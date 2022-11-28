# Strings / localization file for greed
# # Düzenlenebilir, ancak YEDEK ALANLARINI ( {curly braces} ) ile çevrili kelimeleri ÇIKARMAYIN

# Para birimi sembolü
currency_symbol = "€"

# Para birimi sembolünün konumlandırılması
currency_format_string = "{symbol} {value}"

# Stoktaki bir ürünün miktarı
in_stock_format_string = "{quantity} kullanılabilir"

# Sepetteki bir ürünün kopyaları
in_cart_format_string = "{quantity} sepet içinde"


# Ürün bilgisi
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Sipariş numarası, sipariş bilgisinde görüntülenir
order_number = "Sipariş #{id}"

# Yöneticilere gösterilen sipariş bilgi dizesi
order_format_string = "by {user}\n" \
                      "üzerinde oluşturuldu {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTAL: <b>{value}</b>\n" \
                      "\n" \
                      "Müşteri notu: {notes}\n"


# Kullanıcıya gösterilen sipariş bilgi dizesi
user_order_format_string = "{status_emoji} <b>Sipariş {status_text}</b>\n" \
                           "{items}\n" \
                           "TOPLAM: <b>{value}</b>\n" \
                           "\n" \
                           "Notlar: {notes}\n"

# İşlem sayfası yükleniyor
loading_transactions = "<i>İşlem Yükleniyor...\n" \
                       "Lütfen birkaç saniye bekleyin.</i>"


# İşlemler sayfası
transactions_page = "Sayfa <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv altyazı
csv_caption = "Bot veritabanında depolanan tüm işlemleri içeren bir 📄 .csv dosyası oluşturuldu.\n" \
              "Bu dosyayı işlemek için LibreOffice Calc gibi diğer programlarla açabilirsiniz" \
              " veri."

# Conversation: start komutu gönderildi ve bot kullanıcıyı karşılamalı
conversation_after_start = "Merhaba!\n"\
                           "Greed'e hoş geldiniz!\n"\
                           "Bu yazılımın  ⁇ ️ < b > Beta < / b > sürümüdür.\n"\
                           "Tamamen kullanılabilir, ancak hala bazı hatalar olabilir.\n"\
                           "Herhangi birini bulursanız, lütfen bunları https://github.com/Steffo99/greed/issues. adresinden bildiriniz"

# Conversation: satır içi klavye göndermek için onunla bir mesaj göndermeniz gerekir
conversation_open_user_menu = "Ne yapmak istersin?\n"\
                              "💰 Cüzdanınızda < b > {credit} </b> var.\n"\
                              "\n" \
                              "<i> Bir işlem seçmek için alt klavyedeki bir tuşa basın.\n" \
                              "Klavye açılmadıysa, dört küçük düğmeye basarak açabilirsiniz" \
                              " mesaj çubuğundaki kareler. </i>"


# Conversation: yukarıdaki gibi, ancak yöneticiler için
conversation_open_admin_menu = "Bu mağazanın 💼 <b> Yöneticisisiniz </b>!\n"\
                               "Ne yapmak istersin?\n"\
                               "\n"\
                               "<i> Bir işlem seçmek için alt klavyedeki bir tuşa basın.\n" \
                               "Klavye açılmadıysa, dört küçük düğmeye basarak açabilirsiniz" \
                               " mesaj çubuğundaki kareler. </i>"
# Conversation: bir ödeme yöntemi seçin
conversation_payment_method = "Cüzdanınıza nasıl para eklemek istiyorsunuz?"

# Conversation: düzenlenecek bir ürün seçin
conversation_admin_select_product = "✏️ Hangi ürünü düzenlemek istiyorsunuz?"

# Conversation: silinecek bir ürün seçin
conversation_admin_select_product_to_delete = "❌ Hangi ürünü silmek istiyorsunuz?"

# Conversation: Düzenlenecek kullanıcıyı seçin
conversation_admin_select_user = "Düzenlenecek bir kullanıcı seçin."

# Conversation: satın alma için ödeme yapmak üzere aşağıya tıklayın
conversation_cart_actions = "<i>Yukarı kaydırarak ve aşağıdaki Ekle düğmesine basarak ürünleri sepete ekleyin" \
                            " sepete eklemek istediğiniz ürünler. İşiniz bittiğinde, bu mesaja geri dönün ve" \
                            " aşağıdaki Bitti düğmesine basın.</i>"

# Conversation: alışveriş sepeti içeriğini onaylayın
conversation_confirm_cart = "🛒 Sepetiniz aşağıdaki ürünleri içeriyor:\n" \
                            "{product_list}" \
                            "Toplam: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Devam etmek istiyorsanız, bu iletinin altındaki Bitti düğmesine basın.\n" \
                            "İptal etmek için İptal düğmesine basın.</i>"

# # Canlı sipariş modu: başlat
conversation_live_orders_start = "Canlı Siparişler <b>Live Orders</b> modundasınız\n" \
                                 ""Müşteriler tarafından verilen tüm yeni siparişler bu sohbette gerçek zamanlı olarak görünecek ve siz" \
                                 " onları ✅ Tamamlandı olarak işaretleyebilecek" \
                                 " veya ✴️ Müşteriden alınan krediyi geri ödeyin."

# Canlı sipariş modu: mesaj almayı durdur
conversation_live_orders_stop = "<i>Durdurmak için bu iletinin altındaki Durdur düğmesine basın" \
                                " besleme.</i>"

# Conversation: yardım menüsü açıldı
conversation_open_help_menu = "Ne tür yardıma ihtiyacınız var?"

# Conversation: yöneticiye promosyonu onaylayın
conversation_confirm_admin_promotion = "Bu kullanıcıyı 💼 Manager'a tanıtmak istediğinizden emin misiniz?\n" \
                                       "Bu geri dönüşü olmayan bir eylem!"

# Conversation:  dil seçim menü başlığı
conversation_language_select = "Bir dil seçin:"

# Conversation:  kullanıcı moduna geçme
conversation_switch_to_user_mode = " 👤 Müşteri moduna geçiyorsunuz.\n" \
                                   "💼 Yönetici menüsüne geri dönmek istiyorsanız, /start komutu ile konuşmayı yeniden başlatın."

# Notification: görüşmenin süresi doldu
conversation_expired = "🕐 Bir süredir mesaj almadım, bu yüzden kaydetmek için konuşmayı kapattım" \
                       " kaynaklar.\n" \
                       "Yeni bir tane başlatmak istiyorsanız, yeni bir / start komutu gönderin."

# Kullanıcı menüsü: sipariş
menu_order = "🛒 Ürün sipariş et"

# Kullanıcı menüsü: sipariş durumu
menu_order_status = "🛍 Siparişlerim"

# Kullanıcı menüsü: kredi ekle
menu_add_credit = "💵 Para ekleyin"

# Kullanıcı menüsü: bot bilgisi
menu_bot_info = "i️ Bot bilgisi"

# Kullanıcı menüsü: nakit
menu_cash = "💵 Nakit ile"

# Kullanıcı menüsü: kredi kartı
menu_credit_card = "💳 Kredi kartıyla"

# Yönetici menüsü: ürünler
menu_products = " ️ Ürünleri"

# Yönetici menüsü: siparişler
menu_orders = "📦 Siparişler"

# Menü: işlemler
menu_transactions = "💳 İşlem listesi"

# Menü: krediyi düzenle
menu_edit_credit = "💰 İşlem oluştur"

# Yönetici menüsü: kullanıcı moduna gidin
menu_user_mode = "👤 Müşteri moduna geç"

# Yönetici menüsü: ürün ekle
menu_add_product = "✨ Yeni ürün"

# Yönetici menüsü: ürünü sil
menu_delete_product = "❌ Ürünü sil"

# Menü: iptal et
menu_cancel = "🔙 İptal"

# Menü: atla
menu_skip = "⏭ Atla"

# Menü: bitti
menu_done = "Zorlama yapıldı"

# Menü: ödeme faturası
menu_pay = "💳 Öde"

# Menü: tamamlandı
menu_complete = "✅ Tamamlandı"

# Menü: geri ödeme
menu_refund = "itiraz iadesi"

# Menü: dur
menu_stop = "🛑 Dur"

# Menü: Sepete ekle
menu_add_to_cart = "➕ Ekle"

# Menü: arabadan kaldır
menu_remove_from_cart = "➖ Kaldır"

# Menü: yardım menüsü
menu_help = "❓ Yardım / Destek"

# Menü: kılavuz
menu_guide = "📖 Kılavuzu"

# Menü: sonraki sayfa
menu_sonraki = "Ligh️ Sonraki"

# Menü: önceki sayfa
menu_previous = "◀ ️ Önceki"

# Menü: dükkân sahibiyle iletişime geçin
menu_contact_shopkeeper = "Mağazaya başvurun"

# Menü: .csv dosyası oluşturma
menu_csv = "📄 .csv"

# Menü: yönetici listesini düzenle
menu_edit_admins = "🏵 Yöneticileri Düzenle"

# Menü: dil
menu_language = "🇬🇧 Dil"

# Emoji: işlenmemiş sipariş
emoji_not_processed = " ️"

# Emoji: sipariş tamamlandı
emoji_completed = "✅"

# Emoji: iade sipariş
emoji_refunded = "Saldırganlık"

# Emoji: evet
emoji_yes = "✅"

# Emoji: hayır
emoji_no = "🚫"

# Metin: işlenmemiş sipariş
text_not_processed = "beklemede"

# Metin: sipariş tamamlandı
text_completed = "tamamlandı"

# Metin: iade edilen sipariş
text_refunded = "yeniden finanse edildi"

# Metin: ürün satılık değil
text_not_for_sale = "Satılık değil"

# Ürün ekle: isim?
ask_product_name = "Ürün adı ne olmalı?"

# Ürün ekle: açıklama?
ask_product_description = "Ürün açıklaması ne olmalı?"

# Ürün ekle: fiyat?
ask_product_price = "Ürün fiyatı ne olmalı?\n" \
                    "Ürünün henüz satışta olmasını istemiyorsanız <code>X</code> girin."

# Ürün ekle: resim?
ask_product_image = "🖼 Ürünün hangi görüntüye sahip olmasını istiyorsunuz?\n" \
                    "\n" \
                    "<i> Fotoğrafı gönderin veya bu aşamayı atlayın ve resim eklemeyin.</i>"

# Sipariş ürünü: notlar?
ask_order_notes ="Siparişle birlikte bir not bırakmak ister misiniz?\n" \
                  "💼 Mağaza Yöneticileri tarafından görülebilir.\n" \
                  "\n" \
                  "<i>Ayrılmak istediğiniz notu içeren bir mesaj gönderin veya bunun altındaki Atla düğmesine basın" \
                  " hiçbir şey bırakma mesajı.</i>"

# Geri ödeme ürünü: nedeni?
ask_refund_reason =" Bu geri ödemeye bir neden ekleyin.\n" \
                    "👤 Müşteri tarafından görülebilir."

# Krediyi düzenle: notlar?
ask_transaction_notes = " Bu işleme bir not ekleyin.\n" \
                        "👤 Kredi / borçlandırıldıktan sonra müşteri tarafından görülebilir"\
                        " ve işlem günlüğündeki 💼 Yöneticilerine."

# Krediyi düzenle: tutar?
ask_credit = "Müşterinin kredisini nasıl değiştirmek istiyorsunuz?\n" \
             "\n" \
             "<i> Miktarı içeren bir mesaj gönderin.\n" \
             "Müşterinin hesabına kredi eklemek için </i><code>+</code><i> işaretini kullanın," \
             " ve </i><code>-</code><i> to deduce it.</i> işareti"

# Yönetici mesajını düzenle başlığı
admin_properties = "<b>izinler {name}:</b>"

# Yönetici düzenle: ürünleri düzenleyebilir mi?
prop_edit_products = "Ürünleri düzenle"
# Yönetici düzenle: sipariş alabilir mi?
prop_receive_orders = "Sipariş al"

# Yönetici düzenle: işlem oluşturabilir mi?
prop_create_transactions = "İşlemleri yönet"


# Yönetici düzenle: yardım mesajında göster?
prop_display_on_help = "Müşteriye göster"

# Konu bir resim indirmeye başladı ve yanıt vermeyebilir
downloading_image = "Fotoğrafını indiriyorum!\n" \
                    "Biraz zaman alabilir... Lütfen sabırlı olun!\n" \
                    "İndirirken size cevap veremeyeceğim."

# Ürünü düzenle: geçerli değer
edit_current_value = "Geçerli değer:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Aynı değeri korumak için bu iletinin altındaki Atla düğmesine basın.</i>"


# Ödeme: nakit ödeme bilgisi
payment_cash = "Mağazanın fiziksel konumundan nakit olarak ödeme yapabilirsiniz.\n" \
               "Kasada ödeme yapın ve bu kimliği yöneticiye verin:\n" \
               "<b>{user_cash_id}</b>"

# Ödeme: fatura tutarı
payment_cc_amount = "Cüzdanınıza kaç para eklemek istiyorsunuz?\n" \
                    "\n" \
                    "<i>Aşağıdaki düğmelerle bir miktar seçin veya normal klavyeyi kullanarak manuel olarak girin.</i>"

# Ödeme: para fatura başlığı ekleyin
payment_invoice_title = "Para ekleme"

# Ödeme: para fatura açıklaması ekleyin
payment_invoice_description = "Bu faturanın ödenmesi cüzdanınıza {amount} ekleyecektir."

# Ödeme: faturadaki etiketli fiyatın etiketi
payment_invoice_label = "Yeniden yükle"

# Ödeme: faturadaki etiketli fiyatın etiketi
payment_invoice_fee_label = "İşlem ücreti"

# Bildirim: sipariş verildi
notification_order_placed = "Yeni bir sipariş verildi:\n" \
                            "\n" \
                            "{order}"

# Bildirim: sipariş tamamlandı
notification_order_completed = "Siparişiniz tamamlandı!\n" \
                               "\n" \
                               "{order}"

# Bildirim: sipariş iade edildi
notification_order_refunded = "Siparişiniz iade edildi!\n" \
                              "\n" \
                              "{order}"

# Bildirim: manuel işlem uygulandı
notification_transaction_created = "ℹ️  Cüzdanınıza yeni bir işlem uygulandı:\n" \
                                   "{transaction}"

# Geri ödeme nedeni
refund_reason = "Geri ödeme nedeni:\n" \
                "{reason}"

# Bilgi: bot bilgisi
bot_info = 'This bot is using <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' Telegram ödemeleri için @Steffo tarafından bir çerçeve \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public License 3.0</a>.\n'

# Yardım: kılavuzu
help_msg = "greed's kılavuzu şu adreste bulunabilir:\n" \
           "https://github.com/Steffo99/greed/wiki"

# Yardım: dükkan sahibi ile iletişime geçin
contact_shopkeeper = "Şu anda, kullanıcı yardımı sağlayabilecek personel aşağıdakilerden oluşmaktadır:\n" \
                     "{shopkeepers}\n" \
                     "<i>Telegram sohbetinde onlarla iletişime geçmek için adlarından birine tıklayın / dokunun.</i>"

# Başarı: ürün veritabanına eklendi / düzenlendi
success_product_edited = "✅ Ürün başarıyla eklendi / değiştirildi!"

# Başarı: ürün veritabanına eklendi / düzenlendi
success_product_deleted = "✅ Ürün başarıyla silindi!"

# Başarı: düzen oluşturuldu
success_order_created = "✅ Sipariş başarıyla gönderildi!\n" \
                        "\n" \
                        "{order}"

# Başarı: sipariş tamamlanmış olarak işaretlendi
success_order_completed = "✅ # {order_id} sırasını tamamlanmış olarak işaretlediniz."

# Başarı: sipariş başarıyla iade edildi
success_order_refunded = "✴️ sipariş #{order_id} iade edildi."

# Başarı: işlem başarıyla oluşturuldu
success_transaction_created = "✅ İşlem başarıyla oluşturuldu!\n" \
                              "{transaction}"

# Hata: özel bir sohbette alınmayan mesaj
error_nonprivate_chat = "⚠️ Bu bot yalnızca özel sohbetlerde çalışır"

# Hata: bir sohbette bir mesaj gönderildi, ancak bu sohbet için çalışan yok.
# /start ile yeni bir işçi oluşturulmasını önerin
error_no_worker_for_chat = "⚠️ Botla konuşma kesintiye uğradı.\n" \
                           "Yeniden başlatmak için /start komutunu bot'a gönderin."
# Hata: Bir sohbette bir mesaj gönderildi, ancak o sohbetin çalışanı hazır değil.
error_worker_not_ready = "🕒 Botla konuşma şu anda başlıyor.\n" \
                         "Lütfen, daha fazla komut göndermeden önce birkaç dakika bekleyin!"

# Hata: fon miktarını maksimum değerin üzerine ekleyin
error_payment_amount_over_max = "⚠️ Tek bir işlemde eklenebilecek maksimum tutar {max_amount} 'dir."

# Hata: min. Altına fon tutarı ekleyin
error_payment_amount_under_min = "⚠️ Tek bir işlemde eklenebilecek minimum tutar {min_amount} 'dir."

# Hata: faturanın süresi doldu ve ödenemiyor
error_invoice_expired = "⚠️ Bu faturanın süresi doldu ve iptal edildi. Hala para eklemek istiyorsanız, Ekle yi kullanın" \
                        " fonlar menu seçeneği."

# Hata: bu isime sahip bir ürün zaten var
error_duplicate_name = "️⚠️ Aynı isime sahip bir ürün zaten var."
# Hata: sipariş vermek için yeterli kredi yok
error_not_enough_credit = "⚠️ Siparişi vermek için yeterli krediniz yok."
# Hata: sipariş zaten temizlendi
error_order_already_cleared = "⚠️  Bu sipariş zaten işleme koyuldu."

# Hata: sipariş verilmedi, bu yüzden hiçbiri gösterilemiyor
error_no_orders = "⚠️  Henüz sipariş vermediniz, bu yüzden görüntülenecek bir şey yok."

# Hata: seçilen kullanıcı mevcut değil
error_user_does_not_exist = "⚠️  Seçilen kullanıcı mevcut değil."

# Ölümcül: konuşma bir istisna yarattı
fatal_conversation_exception = "☢️ Oh hayır! An <b>hata</b> bu konuşmayı kesintiye uğrattı\n" \
                                "Hata, bot sahibine bildirildi, böylece düzeltebilir.\n" \
                                "Konuşmayı yeniden başlatmak için /start komutunu tekrar gönderin."