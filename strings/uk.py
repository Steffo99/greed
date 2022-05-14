# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Currency symbol
currency_symbol = "₴"

# Positioning of the currency symbol
currency_format_string = "{value} {symbol}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} наявні"

# Copies of a product in cart
in_cart_format_string = "{quantity} в кошику"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Замовлення #{id}"

# Order info string, shown to the admins
order_format_string = "Користувач {user}\n" \
                      "Створено {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "ЗАГАЛОМ: <b>{value}</b>\n" \
                      "\n" \
                      "Нотатка: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Замовлення {status_text}</b>\n" \
                           "{items}\n" \
                           "Загалом: <b>{value}</b>\n" \
                           "\n" \
                           "Нотатка: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Завантажую транзакції...\n" \
                       "Зачекайте кілька секунд.</i>"

# Transactions page
transactions_page = "Сторінка <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "Файл 📄 .csv, який має всі транзакції з бази даних бота було сгенеровано.\n" \
              "Можете відкрити файл за допомогою LibreOffice Calc, щоб переглянути деталі."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Привіт!\n" \
                           "Вітаю в greed!\n" \
                           "Це 🅱️ <b>Бета</b> версія програми.\n" \
                           "Програма повністю придатна до використання, але ще можуть бути баги.\n" \
                           "Якщо знайшли баг - повідомте на https://github.com/Steffo99/greed/issues."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Щоб ви хотіли зробити?\n" \
                              "💰 У вас <b>{credit}</b> в гаманці.\n" \
                              "\n" \
                              "<i>Виберіть опцію з варіантів на клавіатурі.\n" \
                              "Якщо клавіатури не видно - її можна активувати кнопкою з чотирма квадратами внизу</i>."

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Ви є 💼 <b>Менеджером</b> цього магазину!\n" \
                               "Що б ви хотіли зробити?\n" \
                               "\n" \
                               "<i>Виберіть опцію з варіантів на клавіатурі.\n" \
                               "Якщо клавіатури не видно - її можна активувати кнопкою з чотирма квадратами внизу</i>."

# Conversation: select a payment method
conversation_payment_method = "Як би Ви хотіли поповнити гаманець?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Який продукт потрібно редагувати?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Який продукт потрібно видалит?"

# Conversation: select a user to edit
conversation_admin_select_user = "Виберіть користувача для редагування."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Додайте продукти в кошик натисканням кнопки Додати." \
                            "  Коли зробите Ваш вибір, повертайтесь до цього повідомлення" \
                            " і натисніть кнопку Готово.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 У вас в кошику наступні продукти:\n" \
                            "{product_list}" \
                            "Всього: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Щоб продовжити натисніть Готово.\n" \
                            "Якщо змінили свою думку - обирайте Відміна.</i>"

# Live orders mode: start
conversation_live_orders_start = "Ви в режимі <b>Свіжі Замовлення</b>\n" \
                                 "Всі нові замовення від покупців зʼявляться в цьому чаті в режимі живого часу," \
                                 " і ви зможете помічати їх ✅ Виконано" \
                                 " або ✴️ Повернути кошти покупцю."

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Натисніть кнопку Стоп в цьому чаті, щоб зупинити цей режим.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Як можемо Вам допомогти?"

# Conversation: language select menu header
conversation_language_select = "Оберіть мову:"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Ви впевнені, що хочете підвищити цього користувача до 💼 Менеджера?\n" \
                                       "Цю дію неможливо відмінити!"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Ви перейшли в режим 👤 Замовника.\n" \
                                   "Якщо хочете повернутись в меню 💼 Менеджера, рестартуйте розмову з /start."

# Notification: the conversation has expired
conversation_expired = "🕐  За довгий час я не отримав жодного повідомлення, тому я завершив розмову" \
                       " щоб зберегти ресурси.\n" \
                       "Щоб почату знову, надішліть команду /start ."

# User menu: order
menu_order = "🛒 Замовлення"

# User menu: order status
menu_order_status = "🛍 Мої замовлення"

# User menu: add credit
menu_add_credit = "💵 Поповнити гаманець"

# User menu: bot info
menu_bot_info = "ℹ️ Інформація про бот"

# User menu: cash
menu_cash = "💵 Готівкою"

# User menu: credit card
menu_credit_card = "💳 Кредитною картою"

# Admin menu: products
menu_products = "📝️ Продукти"

# Admin menu: orders
menu_orders = "📦 Замовлення"

# Menu: transactions
menu_transactions = "💳 Список транзакцій"

# Menu: edit credit
menu_edit_credit = "💰 Створити транзакцію"

# Admin menu: go to user mode
menu_user_mode = "👤 Режим замовника"

# Admin menu: add product
menu_add_product = "✨ Новий продукт"

# Admin menu: delete product
menu_delete_product = "❌ Видалити продукт"

# Menu: cancel
menu_cancel = "🔙 Відміна"

# Menu: skip
menu_skip = "⏭ Пропустити"

# Menu: done
menu_done = "✅️ Готово"

# Menu: pay invoice
menu_pay = "💳 Заплатити"

# Menu: complete
menu_complete = "✅ Готово"

# Menu: refund
menu_refund = "✴️ Повернення коштів"

# Menu: stop
menu_stop = "🛑 Стоп"

# Menu: add to cart
menu_add_to_cart = "➕ Додати"

# Menu: remove from cart
menu_remove_from_cart = "➖ Прибрати"

# Menu: help menu
menu_help = "❓ Допомога"

# Menu: guide
menu_guide = "📖 Інструкція"

# Menu: next page
menu_next = "▶️ Наступна"

# Menu: previous page
menu_previous = "◀️ Попередня"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Контакти магазину"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: language
menu_language = "🇺🇦 Мова"

# Menu: edit admins list
menu_edit_admins = "🏵 Редагувати менеджерів"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "очікує"

# Text: completed order
text_completed = "завершено"

# Text: refunded order
text_refunded = "повернуто"

# Text: product not for sale
text_not_for_sale = "Не продається"

# Add product: name?
ask_product_name = "Як назвати продукт?"

# Add product: description?
ask_product_description = "Який буде опис продукту?"

# Add product: price?
ask_product_price = "Яка буде ціна?\n" \
                    "Введіть <code>X</code> Якщо продукт зараз не продається."

# Add product: image?
ask_product_image = "🖼 Яку картинку додати до продукта?\n" \
                    "\n" \
                    "<i>Надішліть фото, або Пропустіть цей крок.</i>"

ask_product_category = "Оберіть категорію товару"

# Order product: notes?
ask_order_notes = "Залишити повідомлення разом з цією покупкою?\n" \
                  "💼 Повідомлення буде доступне Менеджеру магазину.\n" \
                  "\n" \
                  "<i>Надішліть Ваше повідомлення, або натисність Пропустити" \
                  " щоб не залишати повідомлення.</i>"

# Refund product: reason?
ask_refund_reason = " Напишіть причину повернення коштів.\n" \
                    "👤  Причина буде доступна замовнику."

# Edit credit: notes?
ask_transaction_notes = " Додайте повідомлення до транзакції.\n" \
                        "👤 Повідомлення буде доступне замовнику після поповнення/списання" \
                        " і 💼 Адміністратору в логах транзакцій."

# Edit credit: amount?
ask_credit = "Як ви хочете змінити баланс замовника?\n" \
             "\n" \
             "<i>Надішліть повідомлення з сумою.\n" \
             "Використовуйте  </i><code>+</code><i> щоб поповнити рахунок," \
             " і знак </i><code>-</code><i> щоб списати кошти.</i>"

# Header for the edit admin message
admin_properties = "<b>Доступи користувача {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Редагувати продукти"

# Edit admin: can receive orders?
prop_receive_orders = "Отримувати замовлення"

# Edit admin: can create transactions?
prop_create_transactions = "Керувати транзакціями"

# Edit admin: show on help message?
prop_display_on_help = "Показувати замовнику"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Я завантажую фото!\n" \
                    "Може зайняти деякий час... Майте терпіння!\n" \
                    "Я не зможу відповідати, поки йде завантаження."

# Edit product: current value
edit_current_value = "Поточне значення:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Натисність Пропустити під цим повідомленням, щоб залишити значення таким.</i>"

# Payment: cash payment info
payment_cash = "Ви можете поповнити готівкою прямо в магазині.\n" \
               "Розрахуйтесь і дайте цей id менеджеру:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "На яку сумму ви хочете поповнити гаманець?\n" \
                    "\n" \
                    "<i>Виберіть сумму із запропонованих значень, або введіть вручну в повідомленні.</i>"

# Payment: add funds invoice title
payment_invoice_title = "Поповнення"

# Payment: add funds invoice description
payment_invoice_description = "Оплата цього рахунку додасть {amount} в ваш гаманець."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Платіж"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Оплата за поповнення"

# Notification: order has been placed
notification_order_placed = "Отримано нове замовлення:\n" \
                            "\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Ваше замовнення успішно завершено!\n" \
                               "\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Ваше замовлення відмінено. Кошти повернуто!\n" \
                              "\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Нова транзакція в вашому гаманці:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Причина повернення:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'Цей бот використовує <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' фреймворк розроблений @Steffo для платежів Телеграм випущений під ліцензією' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public License 3.0</a>.\n'

# Help: guide
help_msg = "Інструкція по greed доступна за цією адресою:\n" \
           "https://github.com/Steffo99/greed/wiki"

# Help: contact shopkeeper
contact_shopkeeper = "Наразі наступні працівники доступні і зможуть допомогти:\n" \
                     "{shopkeepers}\n" \
                     "<i>Виберіть когось одного і напишіть в Телеграм чат.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Продукт успішно створено/оновлено!"

# Success: product has been marked as deleted in the database
success_product_deleted = "✅ Продукт успішно видалено!"

# Success: order has been created
success_order_created = "✅ Замовлення успішно надіслано!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Ваше замовлення #{order_id} було успішно проведено."

# Success: order was refunded successfully
success_order_refunded = "✴️ Кошти по замовленню #{order_id} було відшкодовано."

# Success: transaction was created successfully
success_transaction_created = "✅ Транзакцію успішно створено!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Цей бот працює тільки в приватних чатах."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ Спілкування з ботом було перервано.\n" \
                           "Щоб почати знову, надішліть боту команду /start "

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ Максимальна сума однієї транзакції {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Мінімальна сума однієї транзакції {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Час дії інвойсу було вичерпано. Якщо все хочете додати кошти - виберіть Додати" \
                        " кошти в меню."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Продукт з таким імʼям вже існує."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ У вас недостатньо коштів, щоб виконати замовлення."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Це замовлення вже було опрацьовано раніше."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  Ви ще не зробили жодного замовлення, тому тут пусто."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  Такого користувача не існує."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Ой лишенько! <b>Помилка</b> перервала нашу розмову\n" \
                               "Про помилку було повідомлено власника бота.\n" \
                               "Щоб почати розмову знову, надішліть команду /start."
