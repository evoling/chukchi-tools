#!/usr/bin/env python3
import ChukchiOrthog
import unittest

class BaseOrthographyTest:
    known_values = [ # {{{
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # 'а
            ("а'ачек", "ʔaacek"), # 'a
            ("инэнъээ'выльын", "inenʔeʔewəlʔən"), # 'в
            ("и'гын", "ʔiɣən"), # 'г
            ("и'егуйгын", "ʔijeɣujɣən"), # 'е
            ("и'и'н", "ʔiʔin"), # 'и
            ("э'йңэв", "ʔejŋew"), # 'й
            ("апаа'кэ", "apaʔake"), # 'к
            ("и'лгын", "ʔilɣən"), # 'л
            ("а'мын", "ʔamən"), # 'м
            ("а'нқавтагнэты", "ʔanqawtaɣnetə"), # 'н
            ("о'птыма", "ʔoptəma"), # 'п
            ("и'рвытгыр", "ʔirwətɣər"), # 'р
            ("ы'сқагтат", "ʔəcqaɣtat"), # 'с
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # 'т
            ("ы'уйгын", "ʔəujɣən"), # 'у
            ("ы'чопта", "ʔəcopta"), # 'ч
            ("э'э'вал", "ʔeʔewal"), # 'э
            ("э'эймит", "ʔeejmit"), # 'э
            ("э'юпичгын", "ʔejupicɣən"), # 'ю
            ("а'ёйпыгыргын", "ʔajojpəɣərɣən"), # 'ё
            ("а'қавалёмың", "ʔaqawaloməŋ"), # 'қ
            ("и'ңъиң", "ʔiŋʔiŋ"), # 'ң
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # а'
            ("а'ачек", "ʔaacek"), # а'
            ("апаа'кэ", "apaʔake"), # аа
            ("авынральын", "awənralʔən"), # ав
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # аг
            ("кавраръаеп", "kawrarʔajep"), # ае
            ("аймыёчгын", "ajməjocɣən"), # ай
            ("вакъон", "wakʔon"), # ак
            ("авынральын", "awənralʔən"), # ал
            ("акамаграка", "akamaɣraka"), # ам
            ("анольатын", "anolʔatən"), # ан
            ("челкаомыткын", "celkaomətkən"), # ао
            ("апаа'кэ", "apaʔake"), # ап
            ("аръапат", "arʔapat"), # ар
            ("расқэвъян", "racqewjan"), # ас
            ("альэқатгыргын", "alʔeqatɣərɣən"), # ат
            ("а'ачек", "ʔaacek"), # ач
            ("йъаяқ", "jʔajaq"), # ая
            ("аёпычьылгын", "ajopəcʔəlɣən"), # аё
            ("въавақ", "wʔawaq"), # ақ
            ("вакъон", "wakʔon"), # ва
            ("рынгииввылгын", "rənɣiiwwəlɣən"), # вв
            ("кавгыргын", "kawɣərɣən"), # вг
            ("вилюптын", "wiluptən"), # ви
            ("кэвйиквин", "kewjikwin"), # вй
            ("акавкэгты", "akawkeɣtə"), # вк
            ("вывлеңыльын", "wəwleŋəlʔən"), # вл
            ("а'ткэвма", "ʔatkewma"), # вм
            ("авноратвака", "awnoratwaka"), # вн
            ("вопқанэлёолгын", "wopqaneloolɣən"), # во
            ("эвпэты", "ewpetə"), # вп
            ("куврэт", "kuwret"), # вр
            ("ивтун", "iwtun"), # вт
            ("ичвуйгын", "icwujɣən"), # ву
            ("вывчелкалгын", "wəwcelkalɣən"), # вч
            ("анңатъытвъат", "anŋatʔətwʔat"), # въ
            ("въавақ", "wʔawaq"), # въ
            ("авынральын", "awənralʔən"), # вы
            ("авэтывақ", "awetəwaq"), # вэ
            ("гиивқэв", "ɣiiwqew"), # вқ
            ("олёвңыток", "olowŋətok"), # вң
            ("айвэчга", "ajwecɣa"), # га
            ("и'ггинив", "ʔiɣɣiniw"), # гг
            ("вылгил", "wəlɣil"), # ги
            ("тэгйиң", "teɣjiŋ"), # гй
            ("эпээпэгкупрэн", "epeepeɣkupren"), # гк
            ("гаглеты", "ɣaɣletə"), # гл
            ("ягмал", "jaɣmal"), # гм
            ("магны", "maɣnə"), # гн
            ("айгоон", "ajɣoon"), # го
            ("пыгпыг", "pəɣpəɣ"), # гп
            ("гролмакы", "ɣrolmakə"), # гр
            ("алвагты", "alwaɣtə"), # гт
            ("гуйгун", "ɣujɣun"), # гу
            ("мигчир", "miɣcir"), # гч
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # гъ
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # гы
            ("а'ёйпыгыргын", "ʔajojpəɣərɣən"), # гы
            # ("тагьяңгыргын", "taɣjaŋɣərɣən"), # гь is not a possible sequence
            ("акытгэмка", "akətɣemka"), # гэ
            ("қэйъигқэй", "qejʔiɣqej"), # гқ
            ("ралеаңатлыңын", "raleaŋatləŋən"), # еа
            ("гыевкы", "ɣəjewkə"), # ев
            ("выегыргын", "wəjeɣərɣən"), # ег
            ("ейвэл", "jejwel"), # ей
            ("а'ачек", "ʔaacek"), # ек
            ("елыел", "jeləjel"), # ел
            ("емык", "jemək"), # ем
            ("выентон", "wəjenton"), # ен
            ("гынмыеп", "ɣənməjep"), # еп
            ("вэлер", "weler"), # ер
            ("аркычеты", "arkəcetə"), # ет
            ("малечгын", "malecɣən"), # еч
            ("пытлеы'гыргын", "pətleʔəɣərɣən"), # еы
            ("чеэкэй", "ceekej"), # еэ
            ("калеёчгын", "kalejocɣən"), # её
            ("еқаақ", "jeqaaq"), # еқ
            ("вывлеңыльын", "wəwleŋəlʔən"), # ең
            ("и'гын", "ʔiɣən"), # и'
            ("иа'м", "iʔam"), # иа
            ("вэливэл", "weliwel"), # ив
            ("игыр", "iɣər"), # иг
            ("еңқиеқ", "jeŋqijeq"), # ие
            ("виин", "wiin"), # ии
            ("қыеқий", "qəjeqij"), # ий
            ("гынник", "ɣənnik"), # ик
            ("вилюптын", "wiluptən"), # ил
            ("имим", "imim"), # им
            ("гымнин", "ɣəmnin"), # ин
            ("гыйип", "ɣəjip"), # ип
            ("илир", "ilir"), # ир
            ("вэлвъит", "welwʔit"), # ит
            ("иумкын", "iumkən"), # иу
            ("гучвичьын", "ɣucwicʔən"), # ич
            ("қэптиюргын", "qeptijurɣən"), # ию
            ("йивиқ", "jiwiq"), # иқ
            ("гивиңит", "ɣiwiŋit"), # иң
            ("аңқаляйвыльын", "aŋqalajwəlʔən"), # йв
            ("гуйгун", "ɣujɣun"), # йг
            ("выйин", "wəjin"), # йи
            ("қаййъаяқ", "qajjʔajaq"), # йй
            ("калетайкыё", "kaletajkəjo"), # йк
            ("ңойңойлыңын", "ŋojŋojləŋən"), # йл
            ("аймыёчгын", "ajməjocɣən"), # йм
            ("мэйнъунэң", "mejnʔuneŋ"), # йн
            ("а'ёйпыгыргын", "ʔajojpəɣərɣən"), # йп
            ("гыройъэлгын", "ɣərojʔelɣən"), # йъ
            ("айылгыгыргын", "ajəlɣəɣərɣən"), # йы
            ("койңын", "kojŋən"), # йң
            ("алёмка", "alomka"), # ка
            ("ваңқытъёкваё", "waŋqətjokwajo"), # кв
            ("мыкгыргын", "məkɣərɣən"), # кг
            ("кивкив", "kiwkiw"), # ки
            ("манэккойңын", "manekkojŋən"), # кк
            ("клёкалгын", "klokalɣən"), # кл
            ("кмиңын", "kmiŋən"), # км
            ("вэлыткованы", "welətkowanə"), # ко
            ("кричмын", "kricmən"), # кр
            ("вытку", "wətku"), # ку
            ("вакъон", "wakʔon"), # къ
            ("ааңкы", "aaŋkə"), # кы
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # кэ
            # ("гылаатгыр", "ɣəlaatɣər"), # typo in source
            ("алваң", "alwaŋ"), # лв
            ("айылгыгыргын", "ajəlɣəɣərɣən"), # лг
            ("вывлеңыльын", "wəwleŋəlʔən"), # ле
            ("вэливэл", "weliwel"), # ли
            ("кэгрилйыръын", "keɣriljərʔən"), # лй
            ("килкил", "kilkil"), # лк
            ("мэлмэл", "melmel"), # лм
            # ("аңъаломом", "aŋʔalomom"), # typo in source
            ("вылпы", "wəlpə"), # лп
            ("тъылран", "tʔəlran"), # лр
            ("колталгын", "koltalɣən"), # лт
            ("вэлчиин", "welciin"), # лч
            ("вэлывэл", "weləwel"), # лы
            ("авынральын", "awənralʔən"), # ль
            ("вилюптын", "wiluptən"), # лю
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # ля
            ("анңэлёгыргын", "anŋeloɣərɣən"), # лё
            ("гытолқыл", "ɣətolqəl"), # лқ
            ("ралкылңыгыргын", "ralkəlŋəɣərɣən"), # лң
            ("армагты", "armaɣtə"), # ма
            ("ы'мвивыт", "ʔəmwiwət"), # мв
            ("йичьэмиттумгын", "jicʔemittumɣən"), # мг
            ("имим", "imim"), # ми
            ("упэкэмйи", "upekemji"), # мй
            ("галгамкын", "ɣalɣamkən"), # мк
            ("кэмлил", "kemlil"), # мл
            ("оммачгын", "ommacɣən"), # мм
            ("гымнин", "ɣəmnin"), # мн
            ("э'мпакы", "ʔempakə"), # мп
            ("мрагты", "mraɣtə"), # мр
            ("палёмтэлыльын", "palomteləlʔən"), # мт
            ("мумкыл", "mumkəl"), # му
            ("камчагты", "kamcaɣtə"), # мч
            ("имъучит", "imʔucit"), # мъ
            ("нэмықэй", "neməqej"), # мы
            ("валёмэты", "walometə"), # мэ
            ("кырымқор", "kərəmqor"), # мқ
            ("лымңэ", "ləmŋe"), # мң
            ("ваннатгыргын", "wannatɣərɣən"), # на
            ("винвэ", "winwe"), # нв
            ("мынгылгын", "mənɣəlɣən"), # нг
            ("манэглелелгын", "maneɣlelelɣən"), # не
            ("гымнин", "ɣəmnin"), # ни
            ("йиңынйиң", "jiŋənjiŋ"), # нй
            ("мэчынкы", "mecənkə"), # нк
            ("ванлягыргын", "wanlaɣərɣən"), # нл
            ("гынмыл", "ɣənməl"), # нм
            ("ваннатгыргын", "wannatɣərɣən"), # нн
            ("анольатын", "anolʔatən"), # но
            ("гытканпын", "ɣətkanpən"), # нп
            ("авынральын", "awənralʔən"), # нр
            ("выентон", "wəjenton"), # нт
            ("гынупыт", "ɣənupət"), # ну
            ("кэнчиқ", "kenciq"), # нч
            ("анъягыргын", "anjaɣərɣən"), # нъ
            ("и'ннын", "ʔinnən"), # ны
            ("нэмықэй", "neməqej"), # нэ
            ("вэнқор", "wenqor"), # нқ
            ("анңатъытвъат", "anŋatʔətwʔat"), # нң
            ("о'мрэты", "ʔomretə"), # о'
            ("ковлёргоор", "kowlorɣoor"), # ов
            ("амрогты", "amroɣtə"), # ог
            ("гоккой", "ɣokkoj"), # ой
            ("вэчоквын", "wecokwən"), # ок
            ("анольатын", "anolʔatən"), # ол
            ("вакъон", "wakʔon"), # он
            ("айгоон", "ajɣoon"), # оо
            ("вопқанэлёолгын", "wopqaneloolɣən"), # оп
            ("вэнқор", "wenqor"), # ор
            ("йыркывакъосқыёлгын", "jərkəwakʔocqəjolɣən"), # ос
            ("гываткота", "ɣəwatkota"), # от
            ("гыргоча", "ɣərɣoca"), # оч
            ("паңъэвңытоы'лён", "paŋʔewŋətoʔəlon"), # оы
            ("ңытоян", "ŋətojan"), # оя
            ("калеткоёлгын", "kaletkojolɣən"), # оё
            ("роқыр", "roqər"), # оқ
            ("пъоңпъоң", "pʔoŋpʔoŋ"), # оң
            ("апаа'кэ", "apaʔake"), # па
            ("қачгыпвъаглыңын", "qacɣəpwʔaɣləŋən"), # пв
            ("гыепгыргын", "ɣəjepɣərɣən"), # пг
            ("гыпильын", "ɣəpilʔən"), # пи
            ("лыпйиквин", "ləpjikwin"), # пй
            ("йъыпкиттэгын", "jʔəpkitteɣən"), # пк
            ("куплен", "kuplen"), # пл
            ("капоталгын", "kapotalɣən"), # по
            ("ныппыльэв", "nəppəlʔew"), # пп
            ("купрэн", "kupren"), # пр
            ("вилюптын", "wiluptən"), # пт
            ("пучьэқэй", "pucʔeqej"), # пу
            ("пчеқалгын", "pceqalɣən"), # пч
            ("нипъэв", "nipʔew"), # пъ
            ("а'ёйпыгыргын", "ʔajojpəɣərɣən"), # пы
            ("айпэты", "ajpetə"), # пэ
            ("вопқанэлёолгын", "wopqaneloolɣən"), # пқ
            ("авынральын", "awənralʔən"), # ра
            ("вырвыр", "wərwər"), # рв
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # рг
            ("вэгрил", "weɣril"), # ри
            ("кэркэр", "kerker"), # рк
            ("мырмыр", "mərmər"), # рм
            ("гырон", "ɣəron"), # ро
            ("мэлгарпойгын", "melɣarpojɣən"), # рп
            ("грулмын", "ɣrulmən"), # ру
            ("аръапат", "arʔapat"), # ръ
            ("вытрын", "wətrən"), # ры
            ("вайынрэ", "wajənre"), # рэ
            ("вэлёмырқалгын", "welomərqalɣən"), # рқ
            ("тангынрырңыгыргын", "tanɣənrərŋəɣərɣən"), # рң
            ("вэтгысқын", "wetɣəcqən"), # сқ
            ("а'тав", "ʔataw"), # та
            ("анңатъытвъат", "anŋatʔətwʔat"), # тв
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # тг
            ("гутилгын", "ɣutilɣən"), # ти
            ("йитйит", "jitjit"), # тй
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # тк
            ("ытлён", "ətlon"), # тл
            ("у'рэтнутэнут", "ʔuretnutenut"), # тн
            ("выентогыргын", "wəjentoɣərɣən"), # то
            ("кытпэкэты", "kətpeketə"), # тп
            ("вытры", "wətrə"), # тр
            ("гаттэ", "ɣatte"), # тт
            ("ивтун", "iwtun"), # ту
            ("вэтчин", "wetcin"), # тч
            ("анңатъытвъат", "anŋatʔətwʔat"), # тъ
            ("анольатын", "anolʔatən"), # ты
            ("вылтэ", "wəlte"), # тэ
            ("мытқымыт", "mətqəmət"), # тқ
            ("у'мйигйин", "ʔumjiɣjin"), # у'
            ("куврэт", "kuwret"), # ув
            ("чуггэкъэли", "cuɣɣekʔeli"), # уг
            ("и'тъуи'т", "ʔitʔuʔit"), # уи
            ("гуйгун", "ɣujɣun"), # уй
            ("кукэңы", "kukeŋə"), # ук
            ("гулюптын", "ɣuluptən"), # ул
            ("льуминэң", "lʔumineŋ"), # ум
            ("вэлынкықун", "welənkəqun"), # ун
            ("купрэн", "kupren"), # уп
            ("курыткульын", "kurətkulʔən"), # ур
            ("гутилгын", "ɣutilɣən"), # ут
            ("йъуун", "jʔuun"), # уу
            ("имъучит", "imʔucit"), # уч
            ("нэрқуқ", "nerquq"), # уқ
            ("эмнуң", "emnuŋ"), # уң
            ("қача", "qaca"), # ча
            ("гучвичьын", "ɣucwicʔən"), # чв
            ("аймыёчгын", "ajməjocɣən"), # чг
            ("а'ачек", "ʔaacek"), # че
            ("и'ңыпчиқ", "ʔiŋəpciq"), # чи
            ("кричмын", "kricmən"), # чм
            ("пэнчолгын", "pencolɣən"), # чо
            ("мачролтакы", "macroltakə"), # чр
            ("мэчтутъытут", "mectutʔətut"), # чт
            ("имчуқ", "imcuq"), # чу
            ("маччьачаңэты", "maccʔacaŋetə"), # чч
            ("вэчыпқат", "wecəpqat"), # чы
            ("аёпычьылгын", "ajopəcʔəlɣən"), # чь
            ("рагъёчачңыгыргын", "raɣjocacŋəɣərɣən"), # чң
            ("аръапат", "arʔapat"), # ъа
            ("итъен", "itjen"), # ъе
            ("вэлвъит", "welwʔit"), # ъи
            ("вакъон", "wakʔon"), # ъо
            ("кэлитъул", "kelitʔul"), # ъу
            ("анңатъытвъат", "anŋatʔətwʔat"), # ъы
            ("въэгты", "wʔeɣtə"), # ъэ
            ("кынъюльын", "kənjulʔən"), # ъю
            ("анъягыргын", "anjaɣərɣən"), # ъя
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # ъё
            ("пытлеы'гыргын", "pətleʔəɣərɣən"), # ы'
            ("ы'вэқуч", "ʔəwequc"), # ы'
            ("гыарэты", "ɣəaretə"), # ыа
            ("вывлеңыльын", "wəwleŋəlʔən"), # ыв
            ("а'ёйпыгыргын", "ʔajojpəɣərɣən"), # ыг
            ("выегыргын", "wəjeɣərɣən"), # ые
            ("илыил", "iləil"), # ыи
            ("выйин", "wəjin"), # ый
            ("выквэчгын", "wəkwecɣən"), # ык
            ("айылгыгыргын", "ajəlɣəɣərɣən"), # ыл
            ("гымнин", "ɣəmnin"), # ым
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # ын
            ("мычеэръыоттоот", "məceerʔəottoot"), # ыо
            ("вэлыпқат", "weləpqat"), # ып
            ("а'а'тгыргын", "ʔaʔatɣərɣən"), # ыр
            ("вэтгысқын", "wetɣəcqən"), # ыс
            ("анңатъытвъат", "anŋatʔətwʔat"), # ыт
            ("аёпычьылгын", "ajopəcʔəlɣən"), # ыч
            ("тыырколгын", "təərkolɣən"), # ыы
            ("рыюльын", "rəjulʔən"), # ыю
            ("кыялгын", "kəjalɣən"), # ыя
            ("аймыёчгын", "ajməjocɣən"), # ыё
            ("нэмықэй", "neməqej"), # ық
            ("вайыңқэн", "wajəŋqen"), # ың
            ("анольатын", "anolʔatən"), # ьа
            ("қльиттъын", "qlʔittʔən"), # ьи
            ("альокэгты", "alʔokeɣtə"), # ьо
            ("гинльун", "ɣinlʔun"), # ьу
            ("авынральын", "awənralʔən"), # ьы
            ("альэқатгыргын", "alʔeqatɣərɣən"), # ьэ
            ("нывэльян", "nəweljan"), # ья
            ("чольёчгын", "coljocɣən"), # ьё
            ("э'выч", "ʔewəc"), # э'
            ("ванэван", "wanewan"), # эв
            ("каңэгты", "kaŋeɣtə"), # эг
            ("никъэен", "nikʔejen"), # эе
            ("нэмықэй", "neməqej"), # эй
            ("конэкон", "konekon"), # эк
            ("вопқанэлёолгын", "wopqaneloolɣən"), # эл
            ("нэмықэй", "neməqej"), # эм
            ("вэймэн", "wejmen"), # эн
            ("выръэпат", "wərʔepat"), # эп
            ("гэрэчьэт", "ɣerecʔet"), # эр
            ("рэсқын", "recqən"), # эс
            ("айпэты", "ajpetə"), # эт
            ("вэчоквын", "wecokwən"), # эч
            ("рэывъитын", "reəwʔitən"), # эы
            ("вээм", "weem"), # ээ
            ("эюлқын", "ejulqən"), # эю
            ("чарэян", "carejan"), # эя
            ("ваңэёчгын", "waŋejocɣən"), # эё
            ("альэқатгыргын", "alʔeqatɣərɣən"), # эқ
            ("гитэнэң", "ɣiteneŋ"), # эң
            ("қэплювичвэт", "qepluwicwet"), # юв
            ("рэлюйыръын", "relujərʔən"), # юй
            ("кувлюк", "kuwluk"), # юк
            ("рыюльын", "rəjulʔən"), # юл
            ("қэлюнгиң", "qelunɣiŋ"), # юн
            ("вилюптын", "wiluptən"), # юп
            ("люрэқ", "lureq"), # юр
            ("тъэютъэй", "tʔejutʔej"), # ют
            ("қэюу", "qejuu"), # юу
            ("кэглючин", "keɣlucin"), # юч
            ("имытлюқэй", "imətluqej"), # юқ
            ("эқэлюң", "eqeluŋ"), # юң
            ("матъяал", "matjaal"), # яа
            ("лявылгын", "lawəlɣən"), # яв
            ("анъягыргын", "anjaɣərɣən"), # яг
            ("аңқаляйвыльын", "aŋqalajwəlʔən"), # яй
            ("таляквын", "talakwən"), # як
            ("кыялгын", "kəjalɣən"), # ял
            ("лылямоқалгын", "ləlamoqalɣən"), # ям
            ("вычгыян", "wəcɣəjan"), # ян
            ("ныляплятъав", "nəlaplatʔaw"), # яп
            ("лыляргын", "ləlarɣən"), # яр
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # ят
            ("мыляч", "məlac"), # яч
            ("лыляэлгычьылгын", "ləlaelɣəcʔəlɣən"), # яэ
            ("галяян", "ɣalajan"), # яя
            ("таляёлгын", "talajolɣən"), # яё
            ("йъаяқ", "jʔajaq"), # яқ
            ("льаляңэтын", "lʔalaŋetən"), # яң
            ("выёвый", "wəjowəj"), # ёв
            ("гылёгты", "ɣəloɣtə"), # ёг
            ("а'ёйпыгыргын", "ʔajojpəɣərɣən"), # ёй
            ("ваңқытъёкваё", "waŋqətjokwajo"), # ёк
            ("агъёляткэгыргын", "aɣjolatkeɣərɣən"), # ёл
            ("колёмэй", "kolomej"), # ём
            ("ытлён", "ətlon"), # ён
            ("вопқанэлёолгын", "wopqaneloolɣən"), # ёо
            ("аёпычьылгын", "ajopəcʔəlɣən"), # ёп
            ("кынъёран", "kənjoran"), # ёр
            ("мэлёталгын", "melotalɣən"), # ёт
            ("аймыёчгын", "ajməjocɣən"), # ёч
            ("вэлёқъолячьын", "weloqʔolacʔən"), # ёқ
            ("амқаёң", "amqajoŋ"), # ёң
            ("альэқатгыргын", "alʔeqatɣərɣən"), # қа
            ("еңқиеқ", "jeŋqijeq"), # қи
            ("ңыроққлеқкав", "ŋəroqqleqkaw"), # қк
            ("мынгытқлеккэн", "mənɣətqlekken"), # қл
            ("вэнқор", "wenqor"), # қо
            ("тақравытрыңран", "taqrawətrəŋran"), # қр
            ("и'қупылқын", "ʔiqupəlqən"), # қу
            ("вэлёқъолячьын", "weloqʔolacʔən"), # қъ
            ("вэлқыл", "welqəl"), # қы
            ("нэмықэй", "neməqej"), # қэ
            ("йыққэй", "jəqqej"), # ққ
            ("анңатъытвъат", "anŋatʔətwʔat"), # ңа
            ("пиңвытрын", "piŋwətrən"), # ңв
            ("райъоңгыргын", "rajʔoŋɣərɣən"), # ңг
            ("гивиңит", "ɣiwiŋit"), # ңи
            ("гытолыңкы", "ɣətoləŋkə"), # ңк
            ("тараңнагчыт", "taraŋnaɣcət"), # ңн
            ("каңолгын", "kaŋolɣən"), # ңо
            ("пъоңпъоң", "pʔoŋpʔoŋ"), # ңп
            ("рэңрэң", "reŋreŋ"), # ңр
            ("леңтымңэ", "leŋtəmŋe"), # ңт
            ("кэңунэң", "keŋuneŋ"), # ңу
            ("вывлеңыльын", "wəwleŋəlʔən"), # ңы
            ("анңэлёгыргын", "anŋeloɣərɣən"), # ңэ
            ("аңқаляйвыльын", "aŋqalajwəlʔən"), # ңқ
            ("вээңңалгын", "weeŋŋalɣən"), # ңң
            ] # }}}

    def assertEqualPairs(self, pairs, funct, reverse=False):
        for original, transformed in pairs:
            if reverse:
                orignal, transformed = transformed, original
            result = funct(original)
            self.assertEqual(transformed, result)


class ToIPA(unittest.TestCase, BaseOrthographyTest):

    def test_normalise(self):
        data = [("қораӊы", "ӄораӈы")]
        self.assertEqualPairs(data, ChukchiOrthog.normalise)

    def test_normalise_typewriter_style(self):
        data = [("к'оран'ы", "ӄораӈы")]
        self.assertEqualPairs(data, ChukchiOrthog.normalise)

    def test_simple_substitution(self):
        data = [("нэрӄуӄ", "nerquq"), ("эмнуӈ", "emnuŋ"), ("ӄача", "qaca")]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    def test_redundant_jotated_vowels(self):
        data = [ 
            ("мыляч", "məlac"),
            ("мэлёталгын", "melotalɣən"),
            ("вывчелкалгын", "wəwcelkalɣən"),
            ("вилюптын", "wiluptən")]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    def test_cq_sequence(self):
        data = [("вэтгысқын", "wetɣəcqən")]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    def test_jotated_vowels_with_vowel(self):
        data = [
                ("ёкваё", "jokwajo"), 
                ]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    def test_jotated_i(self):
        data = [("кэвйиквин", "kewjikwin")]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    def test_jotated_vowels_with_hardsoft(self):
        data = [("анъягыргын", "anjaɣərɣən"), ]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    def test_unjotated_vowels_with_hardsoft(self):
        data = [("вывлеңыльын", "wəwleŋəlʔən"),]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    def test_apostrophe(self):
        data = [
            ("и'гын", "ʔiɣən"), 
            ("апаа'кэ", "apaʔake"), 
            ("о'птыма", "ʔoptəma"), 
            ("ы'сқагтат", "ʔəcqaɣtat"),
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_ipa)

    # @unittest.skip("complete")
    def test_complete(self):
        self.assertEqualPairs(self.known_values, ChukchiOrthog.to_ipa)
        pass

    
class ToCyrillic(unittest.TestCase, BaseOrthographyTest):

    known_values = [(value, ChukchiOrthog.normalise(key)) for (key, value) in
            BaseOrthographyTest.known_values]

    def test_initial_glottal(self):
        data = [
            ("ʔiɣən", "и'гын"), 
            ("ʔoptəma", "о'птыма"), 
            ("ʔəcqaɣtat", "ы'сӄагтат"),
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_vowel_glottal_sequence(self):
        data = [("apaʔake", "апаа'кэ")]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_consonant_glottal_sequence(self):
        data = [
            ("awənralʔən", "авынраԓьын"),
            ("anolʔatən", "аноԓьатын"),
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_cq_sequence(self):
        data = [
            ("wetɣəcqən", "вэтгысӄын"),
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_jotated_vowel_allographs(self):
        data = [
            ("maneɣlelelɣən", "манэгԓеԓеԓгын"),
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_jotated_i(self):
        data = [("kewjikwin", "кэвйиквин")]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_initial_or_vowel_then_j_sequence(self):
        data = [
            ("jokwajo", "ёкваё"), 
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)
    
    def test_consonant_j_sequence(self):
        data = [
            ("anjaɣərɣən", "анъягыргын"),
            ("nəweljan", "нывэԓьян"),
            ("coljocɣən", "чоԓьёчгын"),
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_ch_vowel_sequence(self):
        data = [
            ("coljocɣən", "чоԓьёчгын"),
            ("arkəcetə", "аркычеты"), # ет
            ("cuɣɣekʔeli", "чуггэкъэԓи"), # уг
            ("carejan", "чарэян"), # эя
            ("mecənkə", "мэчынкы"), # нк
            ]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_initial_ikratkoe(self):
        data = [("jʔajaq", "йъаяӄ")]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    def test_final_ikratkoe(self):
        data = [("ceekej", "чеэкэй")]
        self.assertEqualPairs(data, ChukchiOrthog.to_cyrillic)

    # @unittest.skip("complete")
    def test_complete(self):
        self.assertEqualPairs(self.known_values, ChukchiOrthog.to_cyrillic)


if __name__ == '__main__':
    unittest.main()

# vim:fdm=marker
