import json
import random
import re

random.seed(33321)

# Raw parsed from PDF
raw_text = """
1. Cihazın kalibrovkası zamanı qaz balonundan nә vaxt istifadә edilir? 
Düzgün cavab: Sensorların dәyişilmәsi, nasos sıradan çıxan zaman, texniki 
xidmәt zamanı 

2. CO hansı qazdır, insan orqanizminә necә tәsir edir? 
Düzgün cavab: Karbon oksidi, qırmızı qan hissәciklәrinә qarışaraq, hava 
çatışmamazlığı әmәlә gәtirir, nәticәdә insan huşunu itirir 

3. LEL – tüstü qazı hansı qazlara aiddir, onun gәmidә mәnbәyi: 
Düzgün cavab: İnsan orqanizminә tәsir edәn zәrәrli qazdır, mәnbәyi baş 
mühәrrik, dizel generatoru, buxarqazan 

4. Cihaz sensorunun sınağı nә vaxt yerinә yetirilir? 
Düzgün cavab: Sensoru dәyişdirәndә, tәzә sensor üçün 5 dәqiqә, işlәnmiş 
sensoru 60 saniyә 

5. Cihazı idarә edәn düymәnin әsas vәzifәlәri: 
Düzgün cavab: Yandırıb-söndürmәk, rәqәmlәri azaldıb-çoxaltmaq, 
kalibrovkanı yerinә yetirmәk, menyuya girmәk 

6. Әl ilә kalibrovka nә zaman yerinә yetirilir? 
Düzgün cavab: Hәr dәfә qaz olan obyekti yoxlamağa gedәndә 

7. Gәmi yük anbarlarında, tanklarında әmәlә gәlәn qaz növlәri: 
Düzgün cavab: Kükürd, karbon, metan qazları 

8. Cihaza ehtiyat giriş nә üçündür? 
Düzgün cavab: İstismar zamanı cihazın yaddaşında yığılan qәza 
mәlumatlarını öyrәnmәk üçün 

9. Cihazın hәyacan siqnalları nә vaxt vә necә özünü göstәrir? 
Düzgün cavab: Nasos, datçiklәr sıradan çıxanda, rәqәmlәr göstәrilәn hәdd 
normasından fәrqli olduqda hәm işıq vә hәm dә sәs siqnalı kimi özünü 
göstәrir 

10. Nasosun hәyacan siqnalı nә zaman baş verir? 
Düzgün cavab: Nasos işlәyәn zaman, süzgәcin(filterin) şlanqın vә nasosun 
çirklәnmәsi zamanı 

11. Partlayış tәhlükәsi olan atmosferdә oksigenin hansı miqdarında cihazın 
kalibrovka edilmәsi mümkündür? 
Düzgün cavab: Oksigenin konsentrasiyası 20, 9% olduqda mümkündür 

12. Cihazın әsas işçi elementlәrin texniki xidmәti zamanı(çirklәnәn zaman) 
onun tәmizlәnmәsi üçün hansı vasitәlәrdәn istifadә olunur? 
Düzgün cavab: Elementlәrin silib tәmizlәnmәsi yalnız içmәli su vә pambıq 
parça olmalıdır 

13. Cihazın “Ok” düymәsinin әsas funksiyaları hansılardır? 
Düzgün cavab: “Ok” düymәsi cihazı aktiv deaktiv, kalibrovka zamanı, 
hәyacan siqnalının söndürülmәsi zamanı, kodun verilmәsi zamanı istifadә 
edilir 

14. Cihazın sensoru çirklәnәndә hansı şәraitdә öz-özünә tәmizlәnir? 
Düzgün cavab: Sensor 10-30 dәqiqә tәmiz havada saxlanıldıqda öz-özünә 
tәmizlәnir 

15. Gәmilәrdә qazölçәn cihazlardan әsas etibarı ilә haralarda istifadә edilir? 
Düzgün cavab: Maşın-qazan şöbәsindә, maye yanacaq olan yerlәrdә, 
kameron şöbәsindә, malyarkada istifadә edilir 

16. Cihaz sәnaye sahәsindә hansı işçi temperaturda işlәyә bilәr? 
Düzgün cavab: Cihazın işçi temperaturu -20 °S-dәn +55 °S-yә qәdәr olur 

17. Nümunә götürmәk üçün istifadә olunan nasos nә zaman sınaq olunur? 
Düzgün cavab: Cihaz aktiv olunduqdan sonra әgәr displeydә “ nasos 
nasazdır” yazısı gәlәrsә 

18. Oksigenin hansı miqdarında cihazlardan istifadә etmәk qadağandır? 
Düzgün cavab: 27.6 % 

19. Cihaz hansı halda yenidәn kalibrovka olunmalıdır? 
Düzgün cavab: Yanar qazların konsentrasiyası normadan fәrqli olduqda  

20. Karbon dioksid qazı ilә zәhәrlәnmәnin әlamәtlәri vә ilk tibbi yardım: 
Düzgün cavab: A vә B bәndindә olduğu kimi, әlavә olaraq yuxuluq, 
hәyacanlıq.Zәrәrçәkәn 24 saat vә ya tam sağalana qәdәr yataq rejiminә 
riayәt etmәlidir 

21. Qaz hәyacan siqnalı nә zaman sönür? 
Düzgün cavab: Qaz mühiti qәbul olunan hәddә qayıtdıqda 

22. Hansı halda nümunә nasosunun “nasazlıq” hәyacan siqnalı çağırmağa 
başlayır? 
Düzgün cavab: Nasosun kalibrovkası tamamlananda, nasos nasaz olduqda 
vә ya kalibr şlanqı bәrkidildikdә,filteri yenisi ilә әvәz etdikdә vә kalibr qazı 
tәtbiq edildikdә 

23. Displeydә nasosun nasazlığını bildirәn xәbәrdarlıqdan sonra, nasosun 
yeniden kalibr olunması nasazlığı aradan qaldırmazsa nә etmәk lazımdır? 
Düzgün cavab: Nasosu yenisi ilә әvәz etmәk lazımdır 

24. Cihazın nasosunun filteri tıxanan zaman , filteri hansı üsulla tәmizlәmәk 
lazımdır? 
Düzgün cavab: Yumşaq tәmiz fırçadan istifadә edәrәk, filter tәmizlәnmәli vә 
tam qurudulduqdan sonra yerinә bәrkidilmәlidir 

25. Nasosun filterini yenisi ilә әvәz edәrkәn hansı ardıcıllığa әmәl etmәk 
lazımdır? 
Düzgün cavab: Detektoru söndürdükdәn sonra “Filips” vintaçanla vintlәri 
boşaldıb, filteri yenisi ilә әvәz etdikdәn sonra vintlәri yenidәn bәrkitmәk 
lazımdır 

26. Dәm qazının hansı konsentrasiyası insan üçün ölüm tәhlükәsi yaradır? 
Düzgün cavab: 1.1 % 

27. Açıq göyәrtәdә baş verәn yanğınlar hansı yanğınsöndürәn vasitәlәrlә 
söndürülür? 
Düzgün cavab: Köpük vә ya su ilә (eyni vaxtda olmamaq şәrti ilә) 

28. Yanan mayelәri hansı odsöndürәn vasitәlәrlә söndürmәk olar? 
1. Köpüklә 
2. Kompakt su ilә 
3. Ümumi tәyinatlı tozla 
4. Karbon qazı ilә 
Düzgün cavab: 1,3,4 

29. Cihazı söndürmәk üçün hansı әmәliyyatı yerinә yetirmәk lazımdır? 
Düzgün cavab: Ok” düymәsini ekranda “OFF” yazısı gәlәnәdәk sıxıb 
saxlamaq lazımdır 

30. “Ok” düymәsini 2 dәfә sürәtlә basmaq hansı әmәliyyatlar zamanı yerinә 
yetirilir? 
Düzgün cavab: Hamısı 

31. Bәzi üzvi maddәlәrin buxarı ( silikonlar, hallogenli karbohidratlar) cihazin 
işinә necә tәsir göstәrir? 
Düzgün cavab: Cihazın işini müvәqqәti lәngidir ki, bu da cihazın işinә mәnfi 
tәsir göstәrir 

32. Bәzi üzvi maddәlәrin buxarı ( silikonlar , hallogenli karbohidratlar) cihazın 
işini müvәqqәti lәngidir ki, hansı әmәliyyatdan sonra cihazın normal fәaliyyәti 
bәrpa olunur? 
Düzgün cavab: Yenidәn kalibrovka edildikdәn sonra cihaz öz normal 
fәaliyyәtini bәrpa edir 

33. Yanar qaz sensoru hәr dәfә çirklәndiricinin, zәhәrli qazların vә ya 
buxarların tәsirinә mәruz qaldıqdan sonra hansı әmәliyyat aparılmalıdır? 
Düzgün cavab: Yanar qaz sensoru mütlәq kalibrovka qazı ilә sınaq 
edilmәlidir 

34. Hansı halda tәkrar kalibrovka etmәyә ehtiyac vardır? 
Düzgün cavab: Qaz dәyәrlәri normadan fәrqlidirsә 

35. Şkalanın istәnilәn qәfil yüksәlmәsi vә ya düşmәsi (xaotik göstәricisi) 
zamanı nә başa düşülür? 
Düzgün cavab: Qaz konsentrasiyasının olduğunu bildirir ki, bu hal tәhlükәli 
mühitdәn xәbәr veri 

36. Detektorun uzun müddәt yanar qaz konsentrasiyası vә havanın tәsirinә 
mәruz qalması zamanı detektorda hansı dәyişikliklәr baş verir? 
Düzgün cavab: Detektorun elementlәri yüklәnir ki, bu hal detektorun iş 
xarakteristikasına mәnfi tәsir göstәrir 

37. Kalibrovka әmәliyyatı tamamlanmamış dayandırılanda ekranda 
(displeydә) hansı işarә(yazı) yazılır? 
Düzgün cavab: CAL ABORTED 

38. Cihazın ekranında (displeydә) “CAL DUE” yazısı hansı әmәliyyatın 
aparılmasını tәlәb edir? 
Düzgün cavab: Cihazın Kalibrovka edilmәsini 

39. Aşağı sәviyyәli hәyacan siqnallarının әlamәtlәri hansılardır? 
Düzgün cavab: Sürәtsiz sәs vә vizual siqnal, ALARM vә müvafiq qaz 
xәtlәri(işarәsi) yanıb sönür , vibro siqnal işә düşür 
"""

distractors = {
    1: ["Batareyanı doldurduqda vә ya displeyi yoxlayarkәn", "Qazanalizatoru yalnız otaq temperaturunda tәmizlәyәrkәn", "Rütubәt sensorunu dәyişәrkәn vә ya proqram yenilәnmәsi zamanı"],
    2: ["Ozon qazıdır, sinir sistemini iflic edib ani olaraq bәdәn hәrarәtini aşağı salır", "Kükürd dioksiddir, ağciyәrlәrdә su toplayıb nәfәsalmanı çәtinlәşdirir", "Metan qazıdır, qanda şәkәrin sәviyyәsini kәskin qaldıraraq şok yaradır"],
    3: ["Oksigenat qrupudur, әsas mәnbәyi gәminin soyuducu sistemidir", "Freon qazıdır, әsasәn hava kondisionerlәri vә ventilyasiya şaxtalarında yaranır", "İnert qazlar sırasındandır, әsas mәnbәyi ballast tankları vә nasos şöbәsidir"],
    4: ["Sensoru dәyişdirәndә, tәzә sensor üçün 30 dәqiqә, işlәnmiş sensoru 5 dәqiqә", "Sensoru yalnız rütubәtli havada dәyişdirәrkәn, tәzә vә işlәnmiş üçün eyni vaxtda (2 dәqiqә)", "Sensorun sınağı yalnız illik yoxlama zamanı, 15 dәqiqә әrzindә yerinә yetirilir"],
    5: ["Yalnız qazın konsentrasiyasını ölçmәk vә batareyanın sәviyyәsini yoxlamaq", "Cihazın sәs siqnalını söndürmәk vә avtomatik tәmizlәmә rejimini işә salmaq", "Displeyin işığını dәyişmәk vә yalnız metan qazının sәviyyәsini yoxlamaq"],
    6: ["Cihazın batareyası tam boşalanda vә ya adapterә qoşulduqda", "Yalnız qapalı yerlәrdә işlәmәk üçün nәzәrdә tutulmuş xüsusi icazә vәrәqәsi aldıqda", "Cihazı yalnız istehsalçı tәrәfindәn yoxlamaya göndәrmәzdәn әvvәl"],
    7: ["Freon, argon, helium qazları", "Ozon, azot oksidi, radon qazları", "Karbonmonoksit (CO) vә hidrogen peroksid buxarları"],
    8: ["Cihazın batareyasını daxili enerjiyә qoşmaq vә şarj etmәk üçün", "Əlavә qaz sensorunu cihaza bağlamaq vә ölçü diapazonunu genişlәndirmәk üçün", "Yalnız sәs siqnalının gücünü artırmaq vә ya vibrasiyanı söndürmәk üçün"],
    9: ["Nasos sönәndә, yalnız ekranda xәbәrdarlıq mәtni çıxır, sәs siqnalı olmur", "Rütubәt hәddi aşanda vә ya cihazın qapağı açıq qaldıqda vizual siqnal verir", "Cihazı kompüterә qoşduqda vә mәlumatları köçürәrkәn fasilәsiz sәs gәlir"],
    10: ["Nasos sönülü vәziyyәtdә olduqda vә yalnız batareyanın enerjisi bitdikdә", "Cihazın ekranında nasazlıq kodu görünәndә vә sensor tәmizlәnәn zaman", "Qazanalizator tәmiz havaya çıxarılan zaman vә şlanq ayrıldıqda"],
    11: ["Oksigenin konsentrasiyası 10.5% olduqda mümkündür", "Oksigenin konsentrasiyası 18.0% olduqda mümkündür", "Oksigenin konsentrasiyası 23.5% olduqda mümkündür"],
    12: ["Elementlәrin silib tәmizlәnmәsi spirtli mәhlul vә xüsusi süngәr olmalıdır", "Elementlәrin silib tәmizlәnmәsi sәnaye asetonu vә quru salfet olmalıdır", "Elementlәrin silib tәmizlәnmәsi yuyucu tozu әlavә edilmiş su vә sintetik parça olmalıdır"],
    13: ["“Ok” düymәsi yalnız displeyin işığını yandırmaq vә tarixi dәyişmәk üçün istifadә edilir", "“Ok” düymәsi cihazı zavod tәnzimlәmәlәrinә qaytarmaq vә dili dәyişmәk üçün istifadә edilir", "“Ok” düymәsi yalnız qazın növünü seçmәk vә yaddaşı tәmizlәmәk üçün istifadә edilir"],
    14: ["Sensor 5-10 dәqiqә qapalı vә qaranlıq yerdә saxlanıldıqda öz-özünә tәmizlәnir", "Sensor 60 dәqiqә әrzindә nәm әsgilә büküldükdә öz-özünә tәmizlәnir", "Sensor mühәrrik yağına salınıb çıxarıldıqdan sonra 15 dәqiqәyә öz-özünә tәmizlәnir"],
    15: ["Yalnız gәmi kapitanının kayutasında vә radiorubkada", "Göyәrtәdә, xilasedici qayıqlarda vә naviqasiya körpüsündә", "Kambuzda, gәmi hospitalında vә sәrnişin salonlarında"],
    16: ["Cihazın işçi temperaturu +10 °S-dәn +40 °S-yә qәdәr olur", "Cihazın işçi temperaturu 0 °S-dәn +30 °S-yә qәdәr olur", "Cihazın işçi temperaturu -40 °S-dәn +85 °S-yә qәdәr olur"],
    17: ["Cihaz sönülü vәziyyәtdә olanda vә tәmiz havaya çıxarıldıqda", "Cihaz yalnız adapterlә elektrikә qoşulduqda vә sınaq rejimindә olduqda", "Displeydә “batareya zәifdir” yazısı gәldikdә vә sensor dәyişdirildikdә"],
    18: ["19.5 %", "21.0 %", "23.5 %"],
    19: ["Cihazın batareyası dәyişdirilәndә vә ya tamamilә şarj edildikdә", "Cihaz təmiz havada sınaqdan keçirildikdə və qaz tapılmadıqda", "Displeyin işığı sönəndə və ya düymələr işləmədikdə"],
    20: ["Ağızda acı dad, gözlәrdә qızartı vә öskürәk. Zәrәrçәkәn dәrhal isti duş almalıdır", "Bәdәndә sәpkilәr, hәrarәtin kәskin qalxması. Zәrәrçәkәn dәrhal soyuq su içmәlidir", "Güclü әzәlә ağrıları vә saç tökülmәsi. Zәrәrçәkәnә ağrıkәsici verilmәlidir"],
    21: ["Cihaz sönülü vәziyyәtә gәtirildikdә vә batareya çıxarıldıqda", "Nasosun filteri dәyişdirildikdә vә sensor tәmizlәndikdә", "Kalibrovka rejiminә keçdikdә vә “Ok” düymәsi basıldıqda"],
    22: ["Batareyanın enerjisi 10%-dәn aşağı düşdükdә vә displey sönәndә", "Cihaz çox soyuq hava şәraitinә (0 °S-dәn aşağı) mәruz qaldıqda", "Cihaz tәmiz havada yoxlandıqda vә hәç bir qaz aşkar olunmadıqda"],
    23: ["Nasosu açıb daxilini quru bezlә tәmizlәmәk vә yenidәn qoşmaq lazımdır", "Cihazı söndürüb batareyasını dәyişdirmәk vә yenidәn sınamaq lazımdır", "Nasosun mühәrrikini yağlamaq vә şlanqı qısaltmaq lazımdır"],
    24: ["Filteri su ilә yumaq, fenlә qurutmaq vә yerinә yapışdırıcı ilә bәrkitmәk lazımdır", "Filteri sәnaye spirti ilә silmәk vә nәm halda yerinә taxmaq lazımdır", "Filteri kompressor vasitәsilә yüksәk tәzyiqli hava ilә üfürmәk lazımdır"],
    25: ["Cihazı yandırmaq, köhnә filteri çәkib çıxarmaq vә yenisini basaraq yerinә salmaq lazımdır", "Batareyanı çıxarmaq, cihazın qapağını tam açmaq vә filteri lehimlәmәk lazımdır", "Cihaz işlәk vәziyyәtdәkәn xüsusi açarla filter qapağını açıb dәyişmәk lazımdır"],
    26: ["0.1 %", "5.0 %", "10.0 %"],
    27: ["Yalnız quru qum vә ya odsöndürәn xüsusi yorğan vasitәsilә", "Halon tipli qazlı yanğınsöndürәnlәrlә", "Yalnız yüksәk tәzyiqli karbon qazı şırnağı ilә"],
    28: ["1, 2", "2, 3, 4", "1, 2, 4"],
    29: ["“Ok” düymәsini bir dәfә qısa basıb, sonra batareyanı çıxarmaq lazımdır", "Cihazın arxasındakı düymәni sәs siqnalı gәlәnәdәk basılı saxlamaq lazımdır", "Displeydә “MENU” yazısı gәldikdә hәr iki yan düymәni eyni vaxtda sıxmaq lazımdır"],
    30: ["Qaz ölçmәni dayandırmaq üçün", "Cihazın batareyasını enerjiyә qoymaq üçün", "Cihazın dilini dәyişdirmәk üçün"],
    31: ["Cihazın hәssaslığını artırır vә kiçik qaz sızıntılarını daha tez aşkar edir", "Cihazın ekranını dondurur vә batareyanın sürәtlә boşalmasına sәbәb olur", "Cihazın yaddaşında olan bütün kalibrovka mәlumatlarını silir"],
    32: ["Cihazın filterlәri tam dәyişdirildikdәn vә nasos yuyulduqdan sonra", "Cihazın batareyası tam boşalıb yenidәn şarj edildikdәn sonra", "Cihaz minimum 24 saat tәmiz havada sönülü halda saxlanıldıqdan sonra"],
    33: ["Sensoru yumaq vә günәş şüaları altında qurudulmaq", "Sensorun hәssaslığını bәrpa etmәk üçün cihaza yüksәk tәzyiqli hava vermәk", "Cihazı tәmiz havada 5 dәqiqә işlәdib, dәrhal sondürmәk"],
    34: ["Cihazın batareyası dәyişdirildikdә vә ya yeni adapterә qoşulduqda", "Displeydә vaxt vә tarix göstәricilәri pozulduqda", "Cihaz tәmiz havada istifadә edildikdә vә qaz konsentrasiyası tapılmadıqda"],
    35: ["Cihazın batareyasının sıradan çıxdığını vә qısaqapanma olduğunu bildirir", "Sensorun mexaniki zәdәlәndiyini vә tәcili dәyişdirilmәsini göstәrir", "Cihazın kalibrovkasının pozulduğunu vә yenidәn tәnzimlәnmәsini tәlәb edir"],
    36: ["Detektorun elementlәri daha hәssas olur vә qazı daha sәrrast ölçür", "Detektorun batareya sәrfiyyatı artır vә sәs siqnalı dayanmır", "Detektorun rәqәmsal ekranı sıradan çıxır vә mәlumat göstәrmir"],
    37: ["CAL ERROR", "CAL FAILED", "CAL SUCCESS"],
    38: ["Cihazın batareyasının dәyişdirilmәsini", "Cihazın yaddaşının tәmizlәnmәsini", "Nasosun filterinin yenisi ilә әvәz olunmasını"],
    39: ["Yüksәk sәsli fasilәsiz siqnal, ekranın qırmızı rәngdә yanması, güclü vibrasiya", "Yalnız ekranda 'WARNING' yazısı görünür, sәs vә vibrasiya işә düşmür", "Qısa aralıqlarla tәk sәs siqnalı, ekran sönür, qazanalizator avtomatik sönür"]
}

def parse_pdf_text():
    questions = []
    current_q_text = ""
    current_a_text = ""
    parsing_mode = 0  # 1 for Q, 2 for A
    
    lines = raw_text.strip().split('\n')
    q_num = 1
    
    # Simple regex based matching
    pattern = re.compile(r'^(\d+)\.\s+(.*)')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        match = pattern.match(line)
        if match:
            # save previous
            if current_q_text and current_a_text:
                questions.append({
                    "id": f"q{q_num:03d}",
                    "question": current_q_text.strip(),
                    "correct": current_a_text.strip()
                })
                q_num += 1
                
            current_q_text = line
            current_a_text = ""
            parsing_mode = 1
        elif line.startswith("Düzgün cavab:"):
            current_a_text = line.replace("Düzgün cavab:", "").strip()
            parsing_mode = 2
        else:
            if parsing_mode == 1:
                current_q_text += " " + line
            elif parsing_mode == 2:
                current_a_text += " " + line

    # add last
    if current_q_text and current_a_text:
        questions.append({
            "id": f"q{q_num:03d}",
            "question": current_q_text.strip(),
            "correct": current_a_text.strip()
        })
        
    return questions

def generate_json():
    parsed_questions = parse_pdf_text()
    
    output_questions = []
    
    for i, pq in enumerate(parsed_questions):
        idx = i + 1
        dist = distractors.get(idx, [f"Distractor 1 for {idx}", f"Distractor 2 for {idx}", f"Distractor 3 for {idx}"])
        
        options = [pq['correct']] + dist
        random.shuffle(options)
        
        correct_letter = ""
        letters = ["A", "B", "C", "D"]
        opts_dict = {}
        for j, opt in enumerate(options):
            opts_dict[letters[j]] = opt
            if opt == pq['correct']:
                correct_letter = letters[j]
                
        output_questions.append({
            "id": pq['id'],
            "question": pq['question'],
            "options": opts_dict,
            "correct_answer": correct_letter,
            "explanation": ""
        })
        
    final_json = {
        "certificate": "Gəmi qazanalizatorları və onların istismari",
        "questions": output_questions
    }
    
    output_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_qazanalizatorlar_v_onlar_n_istismar.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=4)
        
    print(f"Successfully wrote {len(output_questions)} questions to {output_path}")

if __name__ == "__main__":
    generate_json()
