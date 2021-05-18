### Game Rating System with Machine Learning (Makine Öğrenmesi ile Oyun Değerlendirme Sistemi)

Oyunun hangi değerlendirme grubuna girdiğine dair [ESRB](https://www.esrb.org/) sistemine göre çıktı verir. Naive Bayes sınıflandırma algoritması kullanılmıştır. Python algoritma kütüphanesi olarak [scikit-learn](https://scikit-learn.org/stable/modules/naive_bayes.html) kullanılmıştır.

[Django](https://www.djangoproject.com/) framework kullanılarak uygulanır.

Aşağıdaki linkten dataset olarak kullanacağımız csv dosyasını indirip, uygulama ana dizinine atın.
```
    https://www.kaggle.com/imohtn/video-games-rating-by-esrb
```
### Kullanımı

Uygulama ana dizininde bir terminal açın ve aşağıdaki komutları yazın.
```
    $ pip install -r requirements.txt
    $ python manage.py runserver
```

### Ekran Görüntüleri

![Page1](https://raw.githubusercontent.com/serdarsari/game-rating-system/master/assets/Gorsel1.png)

![Page2](https://raw.githubusercontent.com/serdarsari/game-rating-system/master/assets/Gorsel2.png)

![Page3](https://raw.githubusercontent.com/serdarsari/game-rating-system/master/assets/Gorsel3.png)
