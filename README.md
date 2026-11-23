# Offline Shop System

Çevrimdışı mağaza sistemi. Ikarus Shop Ultimate altyapısı üzerine yenilenmiş arayüz: mağaza yönetim paneli, mağaza kasası, teklifler, açık artırma, bildirimler, fiyat geçmişi ve mağazada arama penceresi.

[![Video](https://img.youtube.com/vi/e806AnBmxKM/maxresdefault.jpg)](https://youtu.be/e806AnBmxKM)

▶ **Tanıtım videosu:** [youtu.be/e806AnBmxKM](https://youtu.be/e806AnBmxKM)

---

## Ne var?

- Dikey mağaza yönetim paneli (5x9 ızgara, 4 sayfa), kilitli hücreler ve Mağaza Anahtarı (51998) ile açma
- Mağaza kasası (5x9, 3 sayfa): satılan eşyaların parası ve geri dönen eşyalar
- Teklif sistemi: eşyaya teklif ver, kabul / red, "Sadece Teklif" fiyat seçeneği
- Reddedilen / iptal edilen teklifin parası kasaya değil karaktere döner (`ENABLE_IKASHOP_OFFER_REFUND`)
- Açık artırma (oluşturma, teklif verme, sahibi paneli)
- Bildirim paneli (satış, teklif, açık artırma, süre bitimi)
- Ortalama piyasa fiyatı ve satış geçmişi, fiyat girerken öneri
- Mağaza dekorasyonu / görünüm (52000), arama premium (51999)
- Mağaza süresini uzatma, mağazayı taşıma
- Mağaza sadece izinli haritalarda kurulur (varsayılan 1 / 21 / 41, kendi krallığının ilk köyü)
- Sohbete mağaza linki: envanterdeki mağaza butonuna ALT + tık
- Mağazada Ara penceresi: kategori listesi, seviye / adet / efsun filtreleri, fiyat değerlendirmesi, sepet ile çoklu satın alma, satıcı adına göre arama (`@isim`), tam ad araması (`=isim`), arama geçmişi
- Minimapte mağazalar, mağaza adlarını gizleme seçeneği, mağaza görüş mesafesi ayarı

## Paket yapısı

```
01. Svn/          → Client & Game source (Ara / Altına ekle patch dosyaları + yeni dosyalar)
02. Client/       → root, uiscript, locale, ikashop ve d_/ymir work görselleri
03. Server/       → MySQL tabloları, item_proto / item_names satırları
Added/            → Değişikliklerin uygulanmış hali (tam dosyalar, karşılaştırma için)
```

## Flagler

**Client** (`Locale_inc.h`):
- `ENABLE_IKASHOP_RENEWAL`
- `EXTEND_IKASHOP_PRO` (bildirimler, süre uzatma, mağaza taşıma)
- `EXTEND_IKASHOP_ULTIMATE` (fiyat ortalaması, dekorasyon, kilitli hücreler, arama premium)
- `ENABLE_IKASHOP_HIDE_SHOP_NAMES`
- `ENABLE_IKASHOP_ENTITIES`

**Game** (`service.h`):
- `ENABLE_IKASHOP_RENEWAL`
- `EXTEND_IKASHOP_PRO`
- `EXTEND_IKASHOP_ULTIMATE`
- `ENABLE_IKASHOP_ENTITIES`
- `IKASHOP_ALLOWED_MAPS` (`{ 1, 21, 41 }`)
- `ENABLE_IKASHOP_OFFER_REFUND`
- `ENABLE_IKASHOP_SEARCH_RENEWAL` (yenilenmiş arama: kategori 32-40, `@` / `=` önekleri, 1 sn arama beklemesi)

Client ve game tarafında aynı isimli flagler birlikte açık olmalı; tek taraf açıkken paket uyumsuzluğu olur.

## Kurulum (kısaca)

1. `01. Svn` altındaki patch dosyalarını kendi source ağacına uygula. Her blokta `// Ara:` satırlarını bul, `// Altına ekle:` kısmını altına ekle. Tam dosya olarak gelenleri (`ikarus_shop*.cpp/.h`, `ClientManagerIkarusShop.cpp`, `IkarusShopCache.*`, `PythonIkarusShop.*`, `PythonNetworkStreamIkarusShop.cpp`, `JsonHelper.h`, `utils.h`) kopyala; `utils.h` / `JsonHelper.h` sende varsa karşılaştırarak birleştir.
2. `01. Svn/Server/Makefile.txt` ve `01. Svn/Client/vcxproj.txt` içindeki dosyaları projelere ekle.
3. `02. Client/root/uiikashop.py` dosyasını pack'e kopyala, diğer `root` / `uiscript` patch dosyalarını (`# Ara:` / `# Altına ekle:`) kendi dosyalarına uygula.
4. `02. Client/locale/<dil>/new_locale_game.txt` satırlarını kendi locale dosyalarının sonuna ekle, `locale/common/item_list.txt` satırlarını item_list'e ekle.
5. `02. Client/ikashop/` klasörünü bir pack'in köküne (`ikashop/...`), `02. Client/d_/ymir work/` görsellerini pack'e (`d:/ymir work/...`) ekle.
6. `03. Server/mysql/player.sql` dosyasını player veritabanına uygula, `03. Server/proto` satırlarını item_proto / item_names dosyalarına ekle.
7. Client + game + db rebuild, pack güncelle.

## Bağımlılıklar

- Sunucu C++20 ile derlenmeli (`-std=c++2a`, `<ranges>`), db tarafında `fmt` kütüphanesi.
- `item.window` sırası: `IKASHOP_OFFLINESHOP`, `IKASHOP_SAFEBOX`, `IKASHOP_AUCTION` client `GameType.h`, game `length.h` ve MySQL enum'unda aynı sırada olmalı.
- `uiikashop.py` Python `random` modülünü kullanır; client `lib` klasöründe `random.pyc` yoksa Python 2.7 `Lib/random.py` dosyasından ekle.
- `TPlayerItem` boyutu client ve server tarafında birebir aynı olmalı (FreeBSD'de `long` 8 bayt; paketlerde `int32_t` kullan).

## Notlar

- Patch'lerde başka sistemlere ait satırlar görürsen (farklı `#ifdef`), o sistem sende yoksa yok say.
- Locale dosyalarında yalnızca bu sisteme ait `IKASHOP_*` anahtarları var. Türkçe dosyalar cp1254.
- İzinli haritaları `service.h` içindeki `IKASHOP_ALLOWED_MAPS` ile değiştirebilirsin.
- Arama penceresi ayrıca **Shop Search System** reposunda da paylaşıldı; iki paket aynı sistemi içerir, birini kurman yeterli.

## Teşekkür

Altyapı: Ikarus Shop (Ikarus Developer). Arayüz yenilemesi, ek özellikler ve düzeltmeler Best Studio.

---

## İletişim

Sorular için Discord'dan yazabilirsin.

| | |
|---|---|
| GitHub | [github.com/ybeststudio](https://github.com/ybeststudio) |
| Discord | [discord.gg/NXmc6JrwYr](https://discord.gg/NXmc6JrwYr) |
| Discord ID | `beststudio` |
| Web | [beststudio.dev](https://www.beststudio.dev/) |
| TurkMMO | [Best Studio](https://forum.turkmmo.com/uye/2104546-best-studio/) |
| YouTube | [@ybeststudio](https://www.youtube.com/@ybeststudiotr) |
| Instagram | [@ybeststudio](https://www.instagram.com/ybeststudio) |
| Facebook | [ybeststudio](https://www.facebook.com/ybeststudio/) |
| Twitter | [@ybeststudio](https://twitter.com/ybeststudio) |
| TikTok | [@ybeststudio](https://tiktok.com/@ybeststudio) |

---

**Best Studio** — Metin2 private server çözümleri
