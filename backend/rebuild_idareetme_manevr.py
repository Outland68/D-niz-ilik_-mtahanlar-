import json
import random
import os

random.seed(33312)

questions_data = [
    {
        "q": "Suya düşmüş adamı xilas etmәk mәqsәdi ilә bir dairә etmә manevri hansı hallarda istifadә olunur?",
        "c": "Gәmidәn adamı suya düşәrkәn görüblәr",
        "d": [
            "Adamın suya düşmәsini heç kim görmәdikdә vә gec mәlum olduqda",
            "Gәmi dar kanalda hәrәkәt edәrkәn toqquşmanın qarşısını almaq üçün",
            "Lövbәr dayanacağında gәmini axıntıya qarşı döndәrmәk mәqsәdilә"
        ]
    },
    {
        "q": "Gәmini idarә edәn vasitәlәri sadalayın:",
        "c": "Sükan qurğusu, sükanaltı qurğusu, maşın teleqrafı, lövbәr qurğusu, daxili rabitә sistemi",
        "d": [
            "Yük kranları, şvartov qurğuları, yedәk burazları, qaldırıcı mexanizmlәr",
            "Buxar qazanları, hava kompressorları, yağ nasosları, separasiya sistemi",
            "Xilasedici qayıqlar, yanğınsöndürmә nasosları, avariya dizel generatoru"
        ]
    },
    {
        "q": "Gәminin axıntıdan dreyfini necә hesablayırlar?",
        "c": "Xәritәdә axıntı üçbucağı çәkilir vә axıntıdan dreyfin bucağı (β) hesablanır",
        "d": [
            "Külәyin istiqamәtini vә sürәtini nәzәrә alaraq dreyf cәdvәllәrindәn seçilir",
            "Lövbәr zәncirinin suya buraxılmış uzunluğuna әsasәn tәyin edilir",
            "Kompasa vә maşın teleqrafının göstәricilәrinә baxaraq müәyyәn edilir"
        ]
    },
    {
        "q": "Gәminin fırlanma mәrkәzinin nöqtәsi sabit sayılırmı?",
        "c": "Gәminin üfüqi müstәvisinin müxtәlif yerlәrindә yerlәşir",
        "d": [
            "Hәmişә gәminin ağırlıq mәrkәzi ilә üst-üstә düşür vә dәyişmәz qalır",
            "Yalnız gәminin korma hissәsindә sükan oxunun üzәrindә yerlәşir",
            "Hәmişә gәminin tәn ortasında, midel şpanqoutunda sabit olaraq qalır"
        ]
    },
    {
        "q": "Gәmi sirkulyasiya edәndә (dönәndә) ilkin anda hansı yana әyilir?",
        "c": "Sükan çevrilәn tәrәfә",
        "d": [
            "Sükanın çevrildiyi tәrәfin әksinә",
            "Gәminin burnu istiqamәtindә önә",
            "Dönmә zamanı heç bir yana әyilmә baş vermir"
        ]
    },
    {
        "q": "Gәminin tormoz yolu hansı mәna daşıyır?",
        "c": "Gәminin sabitlәşmiş önә әn tam sürәt rejimindәn, arxaya әn tam sürәt rejiminә komanda verildikdәn sonra, tam dayanma anına qәdәr yolu",
        "d": [
            "Lövbәr atıldıqdan sonra gәminin külәk axını ilә sürüklәndiyi mәsafә",
            "Gәminin limana daxil olarkәn lövbәr stansiyasına qәdәr getdiyi mәsafә",
            "Mühәrrik söndürüldükdәn sonra gәminin sәrbәst hәrәkәt etdiyi mәsafә"
        ]
    },
    {
        "q": "Gәminin suya oturumu necә tәyin olunur?",
        "c": "Gәmi korpusunun burun, arxa vә midel tәrәflәrindә yerlәşәn yük markalarına görә",
        "d": [
            "Gәminin texniki pasportunda göstәrilәn daimi kәmiyyәtlәrә әsasәn",
            "Yalnız xoxolotun ölçdüyü dәrinlik fәrqinә әsasәn müәyyәn edilir",
            "Trümdәki suyun sәviyyәsini ölçәn sensorların mәlumatlarına görә"
        ]
    },
    {
        "q": "Standart manevrlәrә nә aiddir?",
        "c": "Gәminin sürәti, sirkulyasiya manevri, qabağa çәkmә, taktiki diametr, “ziqzaq” manevri üzrә sınaqlar, tormoz yolu",
        "d": [
            "Lövbәrә durma, şvartovka әmәliyyatları, yedәklәmә vә bunkerkәrә mәrhәlәlәri",
            "Gәminin ballast sularının dәyişdirilmәsi, yük әmәliyyatları vә trüm yuyulması",
            "Axtarış vә xilasetmә әmәliyyatları, radiolaq manevrlәri vә külәk sınaqları"
        ]
    },
    {
        "q": "Gәminin manevr elementlәrinә nә aiddir?",
        "c": "İti getmә (yeyinlik), sirkulyasiya qabiliyyәti, inersiya",
        "d": [
            "Yükdaşıma hәcmi, ballast sularının miqdarı, yanacaq sәrfiyyatı",
            "Gәminin uzunluğu, eni vә körpücükdәki avadanlıqların sayı",
            "Lövbәr zәncirinin uzunluğu, şvartov kәndirlәrinin qalınlığı"
        ]
    },
    {
        "q": "Sirkulyasiyanın (dönmәnin) elementlәrinә nә aiddir?",
        "c": "Qabağa çәkmә, taktiki diametr, sabitlәşmiş diametr, tam sirkulyasiya dövrü",
        "d": [
            "Gәminin yırğalanma tezliyi, diferenti, metamsentrik hündürlüyü",
            "Lövbәrin qaldırılma vaxtı, mühәrrikin revers müddәti, fırlanma sürәti",
            "Pәrvanәnin fırlanma momenti, şaftın uzunluğu, sükan oxunun bucağı"
        ]
    },
    {
        "q": "Gәminin “ziqzaq” manevri üzrә sınaqlarda sükanı çevirmә bucağı vә istiqamәtin dәyişmә dәrәcәsi nә qәdәr olmalıdır?",
        "c": "10°/10°",
        "d": [
            "20°/20°",
            "5°/15°",
            "35°/35°"
        ]
    },
    {
        "q": "Gәminin lövbәrdә dayanmağı üçün dәniz dibinin әlverişli tәrkibi hansı sayılır?",
        "c": "Gil, daşlıq",
        "d": [
            "Yumşaq lil, qum",
            "Qayaaltı sәth, mərcan qayaları",
            "Dәrin yarğanlar, vulkanik mәnşәli dib"
        ]
    },
    {
        "q": "Gәmi lövbәrdә dayanarkәn, tәhlükәsiz dayanacaq akvatoriyasının radiusunun miqdarı nәdәn asılıdır?",
        "c": "Gәminin vә suya buraxılan lövbәr zәncirinin uzunluğundan",
        "d": [
            "Lövbәrin ağırlığından vә dәniz suyunun duzluluğundan",
            "Gәminin yük tutumundan vә mühәrrikin gücündәn",
            "Yalnız külәyin vә dәniz dalğalarının gücündәn"
        ]
    },
    {
        "q": "“Fertoinq” üsulu ilә gәmi lövbәrә dayanarkәn, lövbәr zәncirlәri arası tövsiyә olunan bucaq nә qәdәr olmalıdır?",
        "c": "180°",
        "d": [
            "90°",
            "45°",
            "30° - 40°"
        ]
    },
    {
        "q": "Gәminin “şprinq”ə qoyulması nә demәkdir?",
        "c": "Gәminin lövbәri dәnizin dibindәn çıxmırsa, onu güclü axıntının kömәyi ilә çıxartmaq",
        "d": [
            "Körpüyә yan alarkәn gәminin burnunu şvartovlarla kәskin şәkildә saxlamaq",
            "Darısqal limanda gәmini mühәrriksiz yedәklәyәrәk yerinә oturtmaq",
            "Gәminin kormasından vә ya burnundan iki zәncirlә eyni anda lövbәr salmaq"
        ]
    },
    {
        "q": "Dayaz sularda üzmə gәminin idarә olunmasına necә tәsir edir?",
        "c": "Suyun müqavimәti artır, dalğalanma proseslәri artır, gәminin sürәti azalır, gәminin orta su oturumu artır",
        "d": [
            "Suyun müqavimәti azalır, gәminin sürәti kәskin artır vә idarәetmә asanlaşır",
            "Gәminin manevr qabiliyyәti artır vә sükanın reaksiyası daha dәqiq olur",
            "Sirkulyasiya diametri kiçilir vә gәminin tormoz yolu xeyli azalır"
        ]
    },
    {
        "q": "Gәmi “brideldә durub” mәnasını açıqlayın:",
        "c": "Gәmi üfüqi vәziyyәtdә olan çәllәyә qoyulub",
        "d": [
            "Gәmi yedәk lülәsinin vasitәsilә başqa gәmiyә bәrkidilib",
            "Gәmi eyni vaxtda dörd lövbәrdәn istifadә edәrәk dayanmışdır",
            "Gәmi tufan zamanı sükanı kilitlәyәrәk dreyf vәziyyәtinә keçib"
        ]
    },
    {
        "q": "Addımı tənzimlənən vint nәdir?",
        "c": "Qanadlarının dönmә bucağını dәyişәn vint",
        "d": [
            "Fırlanma istiqamәtini avtomatik tәnzimlәyәn hәrәkәt mexanizmi",
            "Gәminin sürәtinә uyğun diametrini böyüdüb kiçildәn pәrvanә",
            "Yalnız mühәrrik söndürüldükdә işlәyәn avariya tormoz vinti"
        ]
    },
    {
        "q": "Diferent gәminin idarә olunmasına necә tәsir edir?",
        "c": "Diferent gәminin burun hissәsinә nә qәdәr çox olarsa, bir o qәdәr onun idarә olunması çәtinlәşir",
        "d": [
            "Korma hissәsinә olan diferent gәminin manevrliyini hәmişә pislәşdirir",
            "Diferentin miqdarı sükanın fәaliyyәtinә heç bir tәsir göstәrmir",
            "Burun diferenti olduqda gәminin inersiyası tamam dәf olunur vә dayanır"
        ]
    },
    {
        "q": "Sirkulyasiya (dönmə) zamanı gәminin sürәti necә dәyişir?",
        "c": "Sürәt tәdricәn azalır",
        "d": [
            "Sürәt tәdricәn artır",
            "Sürәt heç dәyişmir vә sabit qalır",
            "Gәmi sirkulyasiyada tamamilә dayanır"
        ]
    },
    {
        "q": "Gәmi körpüdә dayanarkәn, onun әsas vә әlavә burazları necә bәrkidilmәlidir?",
        "c": "Şәraitdәn asılı olaraq bu әmәliyyata gәmi kapitanı göstәriş verir",
        "d": [
            "Hәmişә ilk növbәdә şprinqlәr verilmәli, sonra prodolnular bәrkidilmәlidir",
            "Bütün kәndirlәr yalnız fır-fıranın barabanına sarınaraq saxlanılmalıdır",
            "Dәniz qaydalarına görә nәzarәt yalnız botsmanın ixtiyarında olmalıdır"
        ]
    },
    {
        "q": "Gәmidә istifadә olunan daxili yanma mühәrriklәrinin revers vaxtı nә qәdәrdir?",
        "c": "Kiçik gәmilәrdә - 5 – 20 saniyә, böyük gәmilәrdә - 1 – 2 dәqiqә",
        "d": [
            "Bütün növ gәmilәrdә standart olaraq 30 saniyәdir",
            "Kiçik gәmilәrdә - 1-2 dәqiqә, böyük gәmilәrdә - 3-5 dәqiqә",
            "Revers hәrәkәti anında hәyata keçirilir vә vaxt tәlәb etmir"
        ]
    },
    {
        "q": "Gәmi hansısa bir sәbәbdәn sağ vә ya sol borta yan vәziyyәtdә olarsa, o zaman bu vәziyyәt onun hərəkətdə idarә olunmasına necә tәsir edir?",
        "c": "Gәminin kursu yan tәrәfdәn әks tәrәfә “qaçır”",
        "d": [
            "Gәminin manevr qabiliyyәti yaxşılaşır vә sirkulyasiya azalır",
            "Gәminin kursu yalnız әyilmә olan tәrәfә meyllәnir",
            "Yan vәziyyәt hәrәkәt xәttinә deyil, ancaq inersiyaya tәsir edir"
        ]
    },
    {
        "q": "Suya düşmüş adamı xilas etmәk mәqsәdi ilә “Şarnov” dönmәsi manevri hansı hallarda istifadә olunur?",
        "c": "Adamın suya düşmәsini heç kim görmәdikdә vә gәmini tez bir zamanda keçmiş yoluna qaytarmaq mәqsәdi ilә",
        "d": [
            "Adamı suya düşәrkәn dәrhal gördükdә vә vizual nәzarәt mümkün olduqda",
            "Gәmi dar boğazlarda olduqda vә sirkulyasiya üçün yer çatışmadıqda",
            "Axtarış üçün digәr gәmilәrdәn vә kömәkçi helikopterlәrdәn istifadә edildikdә"
        ]
    },
    {
        "q": "Suya düşmüş adamı xilas etmәk mәqsәdi ilә “Vilyamson” dönmәsi manevri hansı hallarda istifadә olunur?",
        "c": "Bütün hallarda istifadә etmәk olar",
        "d": [
            "Yalnız gәmi lövbәrdәn çıxarkәn baş vermiş hadisәlәrdә",
            "Yalnız hәrәkәtin bölünmәsi sxemindәn kәnarda olduqda",
            "Adam suya düşdüyü an dәrhal mәlum olmadıqda vә qaranlıqda"
        ]
    },
    {
        "q": "Gәminin külәkdәn dreyfini necә hesablayırlar?",
        "c": "Külәyin hәqiqi istiqamәtini vә sürәtini hesablayaraq, gәminin dreyf cәdvәlindәn dreyf bucağı (α) seçilir",
        "d": [
            "Lövbәr zәncirinin suya buraxılmış uzunluğuna әsasәn ölçülür",
            "Sükanın dönmә bucağı vә mühәrrikin dövrlәr sayı ilә tәyin edilir",
            "Xәritәdә axıntı üçbucağı çәkilir vә yalnız suyun istiqamәti nәzәrә alınır"
        ]
    },
    {
        "q": "Gәminin fırlanma mәrkәzi nәdir?",
        "c": "Gәminin üfüqi müstәvisindә yerlәşәn qüvvә nöqtәsidir",
        "d": [
            "Gәminin tәmәr mәrkәzi ilә sükan pәrinin arasındakı orta xәtdir",
            "Sükan qurğusunun oxu vә pәrvanәnin ortası kәsişәn nöqtәdir",
            "Gәmi sirkulyasiya edәrkәn sürәtin sıfıra düşdüyü hәndәsi nәzәri nöqtәdir"
        ]
    },
    {
        "q": "İnersiya gәminin hansı hәrәkәt rejimlәrindә tәyin olunur?",
        "c": "Sabitlәşmiş önә әn tam sürәt rejimindә, “stop” komandası verildikdәn sonra, tam dayanan anına qәdәr",
        "d": [
            "Gәmi lövbәrә durarkәn zәncirin dartılması vә buraxılması aralığında",
            "Sükanın 35 dәrәcә çevrildiyi andan gәminin tam sirkulyasiya etmәsinә qәdәr",
            "Gәminin körpüyә yan alma sürәtindәn tәdricәn şvartovka yerinә çatmasına qәdәr"
        ]
    },
    {
        "q": "Gәminin manevr elementlәri barәdә informasiya hansı sәnәdlәrdә göstәrilmәlidir?",
        "c": "Losman (bәlәdçi) vərəqəsində, manevr elementlәrinin cәdvәlindә, manevr xüsusiyyәtlәrinin formulyarında",
        "d": [
            "Gәminin sanitar vә radiostansiya qeydiyyatı jurnallarında",
            "Yük manifestindә vә tәhlükәsizlik әmәliyyatları üzrә tәlimatda",
            "Maşın şöbәsinin jurnalında vә bunker әmәliyyatları blankında"
        ]
    },
    {
        "q": "İnersiya elementlәrinә nә aiddir?",
        "c": "Mәsafә vә vaxt",
        "d": [
            "Sürәt vә diferent",
            "Lövbәr zәncirinin uzunluğu vә çәkisi",
            "Suyun müqavimәti vә külәyin istiqamәti"
        ]
    },
    {
        "q": "Gәminin sirkulyasiya elementlәri tәyin edilәrkәn, sükanı çevirmә bucağı nә qәdәr olmalıdır?",
        "c": "35°",
        "d": [
            "10°",
            "15°",
            "20°"
        ]
    },
    {
        "q": "Gәmi lövbәr dayanacağı seçәrkәn, әlverişli dәrinliklәr hansılar sayılır?",
        "c": "20-30m",
        "d": [
            "5-10m",
            "50-80m",
            "100-150m"
        ]
    },
    {
        "q": "Gәmi lövbәrdə dayanarkən, istiqamәti hansı tәrәfә olmalıdır?",
        "c": "Külәk vә axıntı istiqamәtinә qarşı; onların eyni zamanda birgә tәsiri olarsa, ikisindәn daha güclü tәsirә qarşı",
        "d": [
            "Hәmişә şimal istiqamәtinә doğru yönәlmәli vә gәminin burnu xәritә meridianına baxmalıdır",
            "Dalğaların gәlmә istiqamәtinә paralel, gәminin börtünü külәyә doğru çevirmәklә",
            "Yalnız dәniz cәrәyanlarının istiqamәtinә yönәlmәli, külәk nәzәrә alınmamalıdır"
        ]
    },
    {
        "q": "Gәmi iki lövbәrә dayanarkәn, lövbәr zәncirlәri arası tövsiyә olunan bucaq nә qәdәr olmalıdır?",
        "c": "30° - 40°",
        "d": [
            "90° - 120°",
            "180°",
            "10° - 15°"
        ]
    },
    {
        "q": "Gәminin lövbәrdә dayanması üçün “Fertoinq” üsulu hansı hallarda istifadә olunur?",
        "c": "Güclü qabarma-çәkilmә axıntılar olan vә mәhdud sahәli akvatoriyalarda",
        "d": [
            "Dәrinliyi 50 metrdәn çox olan açıq dәniz reyidlәrindә dayanarkәn",
            "Buz şəraitində gәminin buzqıran gәmisini gözlәmәsi lazım olduqda",
            "Şiddәtli qasırğa zamanı açıq sular üzәrindә dreyf etmәmәk üçün"
        ]
    },
    {
        "q": "Gәmi lövbәrә dayanarkәn, “lövbәr dayanacağının planşeti” nә üçün çәkilir?",
        "c": "Gәminin tәyin edilmiş yerinə, onun dәyişilmәsinə, naviqasiya cәhәtdәn tәhlükәsizliyinә nәzarәt mәqsәdi ilә",
        "d": [
            "Lövbәr mexanizminin fәaliyyәtini yoxlamaq vә texniki jurnala qeyd etmәk üçün",
            "Körpücükdәn lövbәr braşpilinin görünüş sahәsini dәqiqlәşdirmәk üçün",
            "Şvartovka planını tәşkil etmәk vә kәndirlәrin sayını tәyin etmәk üçün"
        ]
    },
    {
        "q": "Hansı üsullarla gәmi korma ilә körpüyә yan ala bilәr?",
        "c": "Sәrbәst şәkildә, şәraitdәn asılı olaraq",
        "d": [
            "Yalnız xüsusi korma yedәklәri vasitәsilә yedәkçilәrin kömәyi ilә",
            "Yalnız külәk quruya tәrәf әsdiyi hallarda, xüsusi şprinqlәr atmaqla",
            "Lövbәr zәncirlәrini tam buraxaraq, burun tәrәfdәn bәrkidilәrәk"
        ]
    },
    {
        "q": "“Bitinq” üsulu ilә yedәklәmә vaxtı, yedәk burazı yedәk olan gәminin hansı hissәsindә bәrkidilir?",
        "c": "Yedәk gәmisindәn yedәk olan gәmiyә iki buraz verilәrәk, onları bak vә ya korma hissәsinә aralayaraq knextlәrdә bәrkidirlәr",
        "d": [
            "Buraz yalnız gәminin burnunda yerlәşәn әsas lövbәr lülәsindәn keçirilәrәk bәrkidilir",
            "Yedәk burazı gәminin börtlәrinә bәrkidilәrәk gәmini fırlanmağa imkan vermәdәn çәkir",
            "Bir qısa buraz kormadan, digәri isә gәminin tәn ortasında midel hissәdә bәrkidilir"
        ]
    },
    {
        "q": "Dar keçidlәrdә vә kanallarda üzmə gәminin idarә olunmasına necә tәsir edir?",
        "c": "Gәminin burnu yaxın sahildәn aralanmaq istәyir, kanalda isә gәmilәr arası sorma (çәkmә) effekti әmәlә gәlir",
        "d": [
            "Suyun dәrinliyi sabit qaldığından gәminin manevr qabiliyyәti yaxşılaşır vә sәviyyә stabil olur",
            "Gәminin burnu hәmişә daha dәrin yerә can atır vә idarәetmә tamamilә asanlaşır",
            "Sahillәr sirkulyasiya diametrini kiçildir vә gәminin tormoz yolu xeyli azalır"
        ]
    },
    {
        "q": "“Sleminq” sözü hansı mәnanı daşıyır?",
        "c": "Gәminin suya baş vurması zamanında dalğaların onun alt hissәsinә zәrbәlәrlә vurulması",
        "d": [
            "Külәyin tәsirindәn gәminin kәskin olaraq yan börtlәrә әyilmәsi vә yırğalanması",
            "Dar kanalda gәminin burnunun dәniz dibinә sürtünmәsi nәticәsindә yavaşlaması",
            "İki gәminin yaxın mәsafәdә keçәrkәn bir-birini hidrodinamik olaraq çәkmәsi"
        ]
    },
    {
        "q": "Gәminin idarәetmәsindә tәnzimlәnәn addım (VRŞ) istifadәsi, onun tormoz yolunun mәsafәsini vә buna sәrf olunan vaxtı dәyişirmi?",
        "c": "Tormoz yolunu vә vaxtı azaldır",
        "d": [
            "Tormoz yolunu artırır, amma vaxtı azaldır",
            "Heç bir dәyişiklik yaratmır vә tәsirsiz qalır",
            "Yalnız vaxtı artırır vә manevri gecikdirir"
        ]
    },
    {
        "q": "Gәmi yük vә ballast altında olduğu zaman, onun sirkulyasiyası necә dәyişir?",
        "c": "Sirkulyasiya diametri çoxalır",
        "d": [
            "Sirkulyasiya diametri azalır",
            "Heç bir dәyişikliyә mәruz qalmır",
            "Dönmә zamanı inersiya qüvvәsi lәğv olur"
        ]
    },
    {
        "q": "Gәmi körpüdә dayanarkәn, onun burazları hansı dartma qüvvәsinә mәruz qalırlar?",
        "c": "Gәminin bort üzrә yuxarı hissәsindәn verilibsә, onda dartma qüvvәsi dә bir o qәdәr yüksәkdir, bort üzrә aşağı tәrәfә dartma qüvvәsi azalır",
        "d": [
            "Bütün kәndirlәr hәmişә eyni bәrabәr dartma qüvvәsinә mәruz qalırlar",
            "Korma hissәsindәki kәndirlәr hәmişә daha az dartma qüvvәsinә tabe olur",
            "Kәndirlәrin dartma qüvvәsi yalnız suyun duzluluğundan vә qabarmadan asılıdır"
        ]
    },
    {
        "q": "Gәmi lövbәrdә dayanarkәn onu döndәrmәk mәqsәdi ilә, eyni zamanda baş mühәrriki istifadә etmәk olarmı?",
        "c": "Olar",
        "d": [
            "Yalnız yedәk gәmisi vasitәsilә hәyata keçirmәk lazımdır",
            "Qәti qadağandır, çünki zәncir qırıla bilәr",
            "Yalnız burun tәrәfә diferent olduqda mümkündür"
        ]
    },
    {
        "q": "Hansı rәhbәr sәnәdin gәmi sürücülüyünün tәhlükәsizliyinә dair tәlәblәrinә görә, dәnizdә gәminin yerinin tәyin etmәsinin diskretliyinә dair tövsiyәlәr verilib?",
        "c": "şturman xidmәtinin tәşkili üzrә tövsiyәlәrdə (РШС-89)",
        "d": [
            "Beynәlxalq Dәniz Tәşkilatının (IMO) sәrnişin daşıma qaydalarında",
            "Liman Nәzarәti vә Tәhlükәsizliyi İdarәsinin daxili nizamnamәsindә",
            "Gәminin beynәlxalq tonnaj sertifikatı әlavәlәrindә"
        ]
    },
    {
        "q": "Gәmi hәrәkәtin bölünmә sisteminә hansı qaydalara әsasәn daxil olmalı və sistemi tәrk etmәlidir?",
        "c": "Hәrәkәtin bölünmә sisteminin başlanğıc v.y. axırıncı nöqtәsindә, əgər bu mümkün deyilsә, bölünmә sisteminin istiqamәti üzrә kiçik bucaq altında",
        "d": [
            "Sistemә istәnilәn yerdәn 90 dәrәcәlik bucaq altında sürәtlә girmәk vә tәrk etmәk mütlәqdir",
            "Hәmişә yalnız mәrkәzi xәtdәn daxil olmalı vә kәskin manevrlәrlә onu tәrk etmәlidir",
            "Gәmi ayrılma zolağından keçәrәk әks istiqamәtli yola birbaşa hәrәkәtlә qoşulmalıdır"
        ]
    },
    {
        "q": "Gәmi hәrәkәtin bölünmә sisteminin üzәrindәn hansı qaydada keçmәlidir?",
        "c": "Zәruri şәraitdә hәrәkәtin bölünmә sisteminin istiqamәtinә 900 bucaq altında keçmәlidir",
        "d": [
            "Hәmişә ümumi axınla eyni istiqamәtdә paralel vә ziqzaq şәklindә keçmәlidir",
            "Yalnız minimum sürәtlә bölünmә zonasının tәn ortasından diaqonal üzrә",
            "Mümkün qәdәr dreyf edәrәk, 45 dәrәcә bucaq altında digәr xәttә keçmәklә"
        ]
    },
    {
        "q": "Gәmilәr hәrәkәtin bölünmә sistemindә üzәrkәn, qaydalara görә hansı üstünlüklәrә malikdirlәr?",
        "c": "Heç bir üstünlüklәri yoxdur",
        "d": [
            "Digәr sulara nisbәtәn üstünlük hüququna malikdirlәr vә yol onlara verilmәlidir",
            "Yalnız yelkәnli gәmilәrә qarşı üstünlüklәri var, motorlu gәmilәr tәhvil verir",
            "Bölünmә sxemindә sürәti az olan gәmilәrin üstünlüyü beynәlxalq qaydalarla tәsdiqlәnir"
        ]
    },
    {
        "q": "“Qak” üsulu ilә yedәklәmә vaxtı, yedәk burazı yedәk gәmisindә harada bәrkidilir?",
        "c": "Yedәk gәmisinin korma hissәsindә",
        "d": [
            "Yedәk gәmisinin burun lövbәr braşpilindә",
            "Yedәk gәmisinin mәrkәzindәki yük kranlarına",
            "Gәminin midel hissәsindәki şvartov knextlәrinә"
        ]
    },
    {
        "q": "“Sancma” üsulu ilә yedәklәmә vaxtı yedәk gәmisi öz işini necә aparır?",
        "c": "Şәraitdәn asılı olaraq, yedәk gәmisi yedәklənən gәmini müxtәlif istiqamәtlәrdәn burun hissәsi ilә itәliyir vә lazımi vәziyyәtә gәtirir",
        "d": [
            "Yedәk gәmisi öz kormasından kәndir verәrәk onu yalnız uzaq mәsafәdәn çәkir",
            "Bütün fәaliyyәtini lövbәr salaraq statik şәkildә vinç vasitәsilә hәyata keçirir",
            "Yedәk gәmisi digәr gәmiyә paralel yan alaraq hәrәkәti birlikdә tәmin edir"
        ]
    },
    {
        "q": "Fırtına zamanı gәmi hansı hallarda fırtınanın tәsirinә daha çox mәruz qalır?",
        "c": "Gәmi dalğaya qarşı laqla dayananda, dalğanın uzunluğu gәminin uzunluğundan çox olanda, gәminin mühәrriklәri “stop” vәziyyәtindә olanda, gәmi öz istiqamәtini xeyli dәyişәndә, sürәti dalğanın sürәtindәn çox vә ya xeyli az olanda, dalğanın zirvәsindә olanda",
        "d": [
            "Gәmi burunla dalğaya qarşı yavaş hәrәkәt etdikdә vә dalğalar hündür olduqda",
            "Gәmi korma hissәsini külәyә doğru çevirib hәrәkәt etdikdә vә mühәrrik tam gücü ilә işlәdikdә",
            "Gәmi dayaz sularda hәrәkәt edәrkәn vә dalğalar yalnız sәth boyunca irәlilәdikdә"
        ]
    },
    {
        "q": "Gәminin helikopterlә birgә işlәməsi üçün, onu açıq göyәrtәdә qәbul etmәk mәqsәdilә hazırlanan sahә neçә metrdәn az olmamalıdır?",
        "c": "5 metr",
        "d": [
            "20 metr",
            "10 metr",
            "15 metr"
        ]
    },
    {
        "q": "Gәmi lövbәrinin oxunun pәncәlәrinә görә dәniz dibinin sәviyyәsindәn qalxan vәziyyәtdә olması, lövbәrin saxlama qüvvәsinə necə təsir edir?",
        "c": "Lövbərin saxlama qüvvəsi azalır",
        "d": [
            "Lövbәrin saxlama qüvvәsi kәskin olaraq artır",
            "Heç bir tәsir göstәrmir, qüvvә sabit qalır",
            "Lövbәr zәnciri qırılana qәdәr qüvvә bәrabәrlәşir"
        ]
    },
    {
        "q": "Niyə “matrosov” lövbәrinin saxlama gücü, “xol” lövbәrinə nisbətən daha çoxdur?",
        "c": "”matrosov” lövbәrinin pәncәlәri onun oxuna daha yaxın yerlәşir",
        "d": [
            "“matrosov” lövbәrinin qolları daha uzun vә ağır olduğu üçün",
            "“xol” lövbәrindә ox olmadığına görә yerә möhkәm yapışmır",
            "“matrosov” lövbәri daha ağır metallurgiya әrintisindәn hazırlanır"
        ]
    },
    {
        "q": "Hansı hallarda beynәlxalq dәniz hüququna әsasәn, açıq dәnizdә hәrbi gәmilәr tәrәfindәn gәmiyə baxış keçirilir?",
        "c": "Әgәr gәmi qanunsuz radio ötürmә (tele ötürmә) ilә mәşğuldursa",
        "d": [
            "Gәmi hәr hansı limana yan almadan açıq dәnizdә yanacaq qәbul etdikdә",
            "Gәminin AIS sistemi vә radiolokasiya stansiyası sıradan çıxdıqda",
            "Gәmi kapitanı müvafiq icazә olmadan naviqasiya işıqlarını söndürdükdә"
        ]
    },
    {
        "q": "Lövbәri vermәklә körpüyә yan almaq olarmı?",
        "c": "Olar",
        "d": [
            "Yalnız fırtınalı havalarda icazә verilir",
            "Beynәlxalq liman qaydaları ilә qadağandır",
            "Mümkün deyil, çünki sirkulyasiya pozulur"
        ]
    },
    {
        "q": "Axtarış-xilasetmә işlәrini apararkәn, tövsiyə olunmuş axtarış sxemlәri hansı sәnәddә göstәrilib?",
        "c": "IAMSAR",
        "d": [
            "MARPOL",
            "SOLAS",
            "ISPS Code"
        ]
    },
    {
        "q": "Suya düşmüş insanı xilas etmәk üçün standart manevrlәrdәn hansı “dәrhal manevr” kimi istifadә olunmur?",
        "c": "Şarnov manevri",
        "d": [
            "Vilyamson manevri",
            "Tәk sirkulyasiya (Dairә) manevri",
            "Bütün sadalananlar dәrhal manevr kimi hәmişә istifadә olunur"
        ]
    },
    {
        "q": "Dәniz axıntılarını yaradan әsas faktorlar hansılardır?",
        "c": "Külәk, atmosfer tәzyiqi, qabarma-çәkilmәnin baş vermәsi",
        "d": [
            "Gәmilәrin hәrәkәti, dәnizaltı kabellәr vә estakadaların olması",
            "Dәniz dibinin relyefi vә süni dәrinlәşdirmә işlәri",
            "Buzlaqların әrimәsi vә gәmilәrin ballast sularının axıdılması"
        ]
    }
]

out_questions = []

for idx, q_info in enumerate(questions_data, start=1):
    q_id = f"q{idx:03d}"
    options = [q_info["c"]] + q_info["d"]
    random.shuffle(options)
    
    opts_dict = {}
    correct_key = ""
    for letter, opt in zip(["A", "B", "C", "D"], options):
        opts_dict[letter] = opt
        if opt == q_info["c"]:
            correct_key = letter
            
    out_questions.append({
        "id": q_id,
        "question": q_info["q"].replace("900 bucaq", "90° bucaq"), # minor fix for 47
        "options": opts_dict,
        "correct_answer": correct_key,
        "explanation": ""
    })

final_json = {
    "certificate": "Gəminin idarə olunması və manevr edilməsi",
    "questions": out_questions
}

target_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_minin_idar_olunmas_v_manevr_edilm_si.json"

os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(final_json, f, indent=4, ensure_ascii=False)

print(f"Successfully wrote {len(out_questions)} questions to {target_path}")
