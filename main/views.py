from django.shortcuts import render
import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB     #sklearn kütüphanesinden Naive Bayes'in Multinomial tipini import ediyorum.
from sklearn.model_selection import train_test_split   #Cross Validation yapabilmem için, sklearn kütüphanesinden bu işi yapacak olan fonksiyonları import ediyorum.
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score   #Confusion matrix, doğruluk oranı, f-measure, recall vb. değerleri otomatik hesaplayan fonksiyonları import ediyorum.


dataframe = pd.read_csv('Video_games_esrb_rating.csv')   #üzerinde çalışacağım CSV dosyasını pandas ile okuyorum.
dataframe = dataframe.drop(['title'], axis=1)      #İlk sütundaki oyun isimlerini değerlendirmeye almayacağım için bu sütunu kaldırıyorum.


X = dataframe.drop(['esrb_rating'], axis=1).values    #En sonda çıktı sınıfı olan esrb_rating sütununu da kaldırıyorum.
y = dataframe['esrb_rating'].values    #Kaldırdığım sınıfları Y adında bir değişkene atıyorum. Girdilerle çıktıları eşleyebilmek için.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)   #Cross Validation işlemini yapan sklearn fonksiyonunu kullanıyorum. test_size parametresi ile %20 sini test, %80'ini eğitim için kullanacağımı belirtmek için 0.2 yazdım.

MultiNB = MultinomialNB()    #sınıflandırıcının bir örneğini oluşturuyorum ki aşağıda kullanabileyim.
MultiNB.fit(X_train, y_train)   # oluşturduğum örneği .fit metoduna girdi ve çıktı trainlerini veriyorum. Ve modeli eğitiyorum.


def dogruluk_oranlari(request):
    y_pred = MultiNB.predict(X_test)    #Doğruluk oranları sayfasında sonuçları gösterebilmem için, oluşturduğum örneğin predict metodunu kullanarak, X_test verilerini veriyorum. Cross Validation'da %20 lık test kısmı bu X_test dediğim.

    metin = str(classification_report(y_test, y_pred))   #bu hazır fonksiyon ile otomatik olarak, f-measure, recall gibi sonuçları elde ediyorum.
    metinE = metin.find('E')
    metinET = metin.find('ET')
    metinM = metin.find('M')
    metinT = metin.find('T', metinET+5)

    metinE = metin[metinE:metinET]
    metinET = metin[metinET:metinM]
    metinM = metin[metinM:metinT]
    metinT = metin[metinT:metin.find('accuracy')]

    print(metinT.strip().split(' '))
    context = {
        'accuracy_score': str(accuracy_score(y_test, y_pred))[:4],   #Doğruluk oranını görmek için bu hazır fonksiyonu kullanıyorum.
        'confusion_matrix': confusion_matrix(y_test, y_pred),  #Confusion matrix'i elde etmek için bu hazır fonksiyonu kullandım.
        'classification_reportE': metinE.strip().split(' '),
        'classification_reportET': metinET.strip().split(' '),
        'classification_reportM': metinM.strip().split(' '),
        'classification_reportT': metinT.strip().split(' ')
    }
    return render(request, 'dogruluk_oranlari.html', context)


def index(request):
    return render(request, 'index.html', {})


def pred(request):
    secilen1 = 1 if request.POST.get('console') != None else 0          ###BU KISIMLAR django web programlama ile ilgilidir.
    secilen2 = 1 if request.POST.get('alcohol_reference') != None else 0
    secilen3 = 1 if request.POST.get('animated_blood') != None else 0
    secilen4 = 1 if request.POST.get('blood') != None else 0
    secilen5 = 1 if request.POST.get('blood_and_gore') != None else 0
    secilen6 = 1 if request.POST.get('cartoon_violence') != None else 0
    secilen7 = 1 if request.POST.get('crude_humor') != None else 0
    secilen8 = 1 if request.POST.get('drug_reference') != None else 0
    secilen9 = 1 if request.POST.get('fantasy_violence') != None else 0
    secilen10 = 1 if request.POST.get('intense_violence') != None else 0
    secilen11 = 1 if request.POST.get('language') != None else 0
    secilen12 = 1 if request.POST.get('lyrics') != None else 0
    secilen13 = 1 if request.POST.get('mature_humor') != None else 0
    secilen14 = 1 if request.POST.get('mild_blood') != None else 0
    secilen15 = 1 if request.POST.get('mild_cartoon_violence') != None else 0
    secilen16 = 1 if request.POST.get('mild_fantasy_violence') != None else 0
    secilen17 = 1 if request.POST.get('mild_language') != None else 0
    secilen18 = 1 if request.POST.get('mild_lyrics') != None else 0
    secilen19 = 1 if request.POST.get('mild_suggestive_themes') != None else 0
    secilen20 = 1 if request.POST.get('mild_violence') != None else 0
    secilen21 = 1 if request.POST.get('no_descriptors') != None else 0
    secilen22 = 1 if request.POST.get('nudity') != None else 0
    secilen23 = 1 if request.POST.get('partial_nudity') != None else 0
    secilen24 = 1 if request.POST.get('sexual_content') != None else 0
    secilen25 = 1 if request.POST.get('sexual_themes') != None else 0
    secilen26 = 1 if request.POST.get('simulated_gambling') != None else 0
    secilen27 = 1 if request.POST.get('strong_janguage') != None else 0
    secilen28 = 1 if request.POST.get('strong_sexual_content') != None else 0
    secilen29 = 1 if request.POST.get('suggestive_themes') != None else 0
    secilen30 = 1 if request.POST.get('use_of_alcohol') != None else 0
    secilen31 = 1 if request.POST.get('use_of_drugs_and_alcohol') != None else 0
    secilen32 = 1 if request.POST.get('violence') != None else 0

    test = np.array([[secilen1, secilen2,secilen3,secilen4,secilen5,secilen6,secilen7,secilen8,secilen9,
    secilen10,secilen11,secilen12,secilen13,secilen14,secilen15,secilen16,secilen17,secilen18,secilen19,secilen20,secilen21,secilen22,secilen23,
    secilen24,secilen25,secilen26,secilen27,secilen28,secilen29,secilen30,secilen31,secilen32]])


    y_pred = MultiNB.predict(test)


    if y_pred == 'E':
        bilgi = "İçerik genellikle her yaş için uygundur. Minimum düzeyde çizgi film, fantezi veya hafif şiddet içerebilir ve / veya nadiren hafif bir dil kullanılabilir."
        context = {'result': 'E.png',
        'bilgi': bilgi}
    elif y_pred == 'ET':
        bilgi = "İçerik genellikle 10 yaş ve üstü için uygundur. Daha fazla çizgi film, fantezi veya hafif şiddet, hafif dil ve / veya minimum müstehcen temalar içerebilir."
        context = {'result': 'ET.png',
        'bilgi': bilgi}
    elif y_pred == 'T':
        bilgi = "İçerik genellikle 13 yaş ve üstü için uygundur. Şiddet, müstehcen temalar, kaba mizah, asgari düzeyde kan, kumar simülasyonu ve / veya nadiren küfür kullanımı içerebilir."
        context = {'result': 'T.png',
        'bilgi': bilgi}
    elif y_pred == 'M':
        bilgi = "İçerik genellikle 17 yaş ve üstü için uygundur. Yoğun şiddet, kan, cinsel içerik ve / veya sert dil içerebilir."
        context = {'result': 'M.png',
        'bilgi': bilgi}

    return render(request, 'sonuc.html', context)
