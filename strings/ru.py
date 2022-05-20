# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Currency symbol
currency_symbol = "₽"

# Positioning of the currency symbol
currency_format_string = "{value} {symbol}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} доступно"

# Copies of a product in cart
in_cart_format_string = "{quantity} в корзине"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Заказ #{id}"

# Order info string, shown to the admins
order_format_string = "Покупатель {user}\n" \
                      "Создано {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "ИТОГО: <b>{value}</b>\n" \
                      "\n" \
                      "Сообщение: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Заказ {status_text}</b>\n" \
                           "{items}\n" \
                           "Итого: <b>{value}</b>\n" \
                           "\n" \
                           "Сообщение: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Загружаю транзакции...\n" \
                       "Это займет несколько секунд.</i>"

# Transactions page
transactions_page = "Страница <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "Файл 📄 .csv сгенерирован, и содержит все транзакции из базы данных бота.\n" \
              "Вы можете открыть этот файт с помощью LibreOffice Calc, чтобы просмотреть детали."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Привет!\n" \
                           "Добро пожаловать в greed!\n" \
                           "Это 🅱️ <b>Бета</b> версия программы.\n" \
                           "Программа полностью готова к использованию, но могут быть баги.\n" \
                           "Если нашли баг - сообщите тут: https://github.com/Steffo99/greed/issues."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Что бы Вы хотели сделать?\n" \
                              "💰 У вас в кошельке <b>{credit}</b>.\n" \
                              "\n" \
                              "<i>Выберите опцию из вариантов на клавиатуре.\n" \
                              "Если клавиатуры не видно - её можно активировать кнопкой с квадратами внизу.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Вы 💼 <b>Менеджер</b> этого магазина!\n" \
                               "Что бы Вы хотели сделать?\n" \
                               "\n" \
                               "<i>Выберите опцию из вариантов на клавиатуре.\n" \
                               "Если клавиатуры не видно - её можно активировать кнопкой с квадратами внизу.</i>"

# Conversation: select a payment method
conversation_payment_method = "Как бы Вы хотели пополнить ваш кошелек?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Какой продукт необходимо отредактировать?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Какой продукт необходимо удалить?"

# Conversation: select a user to edit
conversation_admin_select_user = "Выберите пользователя для редактирования."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Добавьте продукты в корзину с помощью кнопки Добавить." \
                            "  Когда сделаете Ваш выбор, возвращайтесь к этому сообщению" \
                            " и нажмите кнопку Готово.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Продукты у Вас в корзине:\n" \
                            "{product_list}" \
                            "Итого: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Нажмите Готово, чтобы продолжить.\n" \
                            "Если передумали - выберите Отмена.</i>"

# Live orders mode: start
conversation_live_orders_start = "Вы в режиме <b>Новые заказы</b>\n" \
                                 "Все новые заказы появятся в этом чате в режиме реального времени," \
                                 " и их можно отметить ✅ Выполнено" \
                                 " или ✴️ Возвращено в случае возврата денег." \
 \
# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Нажмите Стоп в этом чате, чтобы остановить этот режим.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Чем могу Вам помочь?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Вы уверены, что хотите повысить этого пользователя до 💼 Менеджера?\n" \
                                       "Это действие невозможно отменить!"
# Conversation: language select menu header
conversation_language_select = "Выберите язык:"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Вы перешли в режим 👤 Покупателя.\n" \
                                   "Если хотите вернутся в режим 💼 Менеджера, рестартуйте с помощью команды /start."

# Notification: the conversation has expired
conversation_expired = "🕐  За долгое время я не получил ни одного сообщения, поэтому я прекратил общение" \
                       " чтобы сохранить ресурсы.\n" \
                       "Чтобы начать снова, пришлите команду /start ."

# User menu: order
menu_order = "🛒 Заказать"

# User menu: order status
menu_order_status = "🛍 Мои заказы"

# User menu: add credit
menu_add_credit = "💵 Пополнить кошелек"

# User menu: bot info
menu_bot_info = "ℹ️ Информация о боте"

# User menu: cash
menu_cash = "💵 Наличными"

# User menu: credit card
menu_credit_card = "💳 Кредитной картой"

# Admin menu: products
menu_products = "📝️ Продукты"

# Admin menu: orders
menu_orders = "📦 Заказы"

# Menu: transactions
menu_transactions = "💳 Список транзакций"

# Menu: edit credit
menu_edit_credit = "💰 Создать транзакцию"

# Admin menu: go to user mode
menu_user_mode = "👤 Режим покупателя"

# Admin menu: add product
menu_add_product = "✨ Новый продукт"

# Admin menu: delete product
menu_delete_product = "❌ Удалить продукт"

# Menu: cancel
menu_cancel = "🔙 Отмена"

# Menu: skip
menu_skip = "⏭ Пропустить"

# Menu: done
menu_done = "✅️ Готово"

# Menu: pay invoice
menu_pay = "💳 Заплатить"

# Menu: complete
menu_complete = "✅ Готово"

# Menu: refund
menu_refund = "✴️ Возврат средств"

# Menu: stop
menu_stop = "🛑 Стоп"

# Menu: add to cart
menu_add_to_cart = "➕ Добавить"

# Menu: remove from cart
menu_remove_from_cart = "➖ Удалить"

# Menu: help menu
menu_help = "❓ Помощь"

# Menu: guide
menu_guide = "📖 Инструкция"

# Menu: next page
menu_next = "▶️ Следующая"

# Menu: previous page
menu_previous = "◀️ Предыдущая"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Контакты"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Изменить менеджеров"

# Menu: language
menu_language = "🇷🇺 Язык"

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
text_not_processed = "ожидает"

# Text: completed order
text_completed = "выполнен"

# Text: refunded order
text_refunded = "возмещен"

# Text: product not for sale
text_not_for_sale = "Не продаётся"

# Add product: name?
ask_product_name = "Как назовем продукт?"

# Add product: description?
ask_product_description = "Каким будет описание продукта?"

# Add product: price?
ask_product_price = "Какова будет цена?\n" \
                    "Введите <code>X</code> если продукт сейчас недоступен."

# Add product: image?
ask_product_image = "🖼 Добавим фото продукта?\n" \
                    "\n" \
                    "<i>Пришлите фото, или Пропустите этот шаг.</i>"

ask_product_category = "Выберите категорию товара"

# Order product: notes?
ask_order_notes = "Оставить заметку к этом заказу?\n" \
                  "💼 Заметка будет доступна Менеджеру магазина.\n" \
                  "\n" \
                  "<i>Напишите Ваше сообщение, или выберите Пропустить," \
                  " чтобы не оставлять заметку.</i>"

# Refund product: reason?
ask_refund_reason = " Сообщите причину возврата средств.\n" \
                    " Причина будет видна 👤 Покупателю."

# Edit credit: notes?
ask_transaction_notes = " Добавьте сообщение к транзакции.\n" \
                        " Сообщение будет доступно 👤 Покупателю после пополнения/списания средств" \
                        " и 💼 Администратору в логах транзакций."

# Edit credit: amount?
ask_credit = "Вы хотите изменить баланс Покупателя?\n" \
             "\n" \
             "<i>Напишите сообщение и укажите сумму.\n" \
             "Используйте </i><code>+</code><i> чтобы пополнить счет," \
             " и знак </i><code>-</code><i> чтобы списать средства.</i>"

# Header for the edit admin message
admin_properties = "<b>Доступы пользователя {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Редактировать продукты"

# Edit admin: can receive orders?
prop_receive_orders = "Получать заказы"

# Edit admin: can create transactions?
prop_create_transactions = "Управлять транзакциями"

# Edit admin: show on help message?
prop_display_on_help = "Показывать покупателям"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Я загружаю фото!\n" \
                    "Это может занять некоторое время...!\n" \
                    "Я не смогу отвечать, пока идет загрузка."

# Edit product: current value
edit_current_value = "Текущее значение:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Нажмите Пропустить, чтобы оставить значение без изменений.</i>"

# Payment: cash payment info
payment_cash = "Вы можете пополнить счет наличными в торговых точках.\n" \
               "Рассчитайтесь и сообщите Менеджеру следующее значение:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "На какую сумму пополнить Ваш кошелек?\n" \
                    "\n" \
                    "<i>Выберите сумму из предложеных значений, или введите вручную в сообщении.</i>"

# Payment: add funds invoice title
payment_invoice_title = "Пополнение"

# Payment: add funds invoice description
payment_invoice_description = "Оплата этого счета добавит {amount} в Ваш кошелек."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Платеж"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Сбор за пополнение"

# Notification: order has been placed
notification_order_placed = "Получен новый заказ:\n" \
                            "\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Ваш заказ успешно выполнен!\n" \
                               "\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Ваш заказ отменен. Средства возвращены в Ваш кошелек!\n" \
                              "\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Новая транзакция в Вашем кошельке:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Причина возврата:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'Этот бот использует <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' фреймворк разработан @Steffo для платежей Телеграм и выпущен под лицензией' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public License 3.0</a>.\n'

# Help: guide
help_msg = "Инструкция к greed доступна по этому адресу:\n" \
           "https://github.com/Steffo99/greed/wiki"

# Help: contact shopkeeper
contact_shopkeeper = "Следующие сотрудники доступны сейчас и могут помочь:\n" \
                     "{shopkeepers}\n" \
                     "<i>Выберите одного из них и напишите в Телеграм чат.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Продукт успешно создан/обновлен!"

# Success: product has been marked as deleted in the database
success_product_deleted = "✅ Продукт успешно удален!"

# Success: order has been created
success_order_created = "✅ Заказ успешно создан!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Ваш заказ #{order_id} был успешно выполнен."

# Success: order was refunded successfully
success_order_refunded = "✴️ Средства по заказу #{order_id} были возвращены."

# Success: transaction was created successfully
success_transaction_created = "✅ Транзакция успешно создана!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Этот бот работает только в частных чатах."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ Общение с ботом было прервано.\n" \
                           "Чтобы начать снова, воспользуйтесь командой /start "

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 Общение с ботом вот-вот начнется.\n" \
                         "Пожалуйста, подождите немного перед отправкой следующей команды!"
                         
# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ Максимальная сумма одной транзакции {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Минимальная сумма одной транзакции {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Время действия инвойса завершено. Если все еще хотите пополнить счет - выберите" \
                        " Пополнить счет в меню."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Продукт с таким именем уже существует."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ У Вас недостаточно средств, чтобы выполнить заказ."

# Error: order has already been cleared
error_order_already_cleared = "⚠️ Этот заказ уже был выполнен ранее."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️ Вы еще не сделали ни одного заказа, поэтому здесь пусто."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️ Нет такого пользователя."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Вот беда! <b>Ошибка</b> прервала наше общение\n" \
                               "Владельцу бота будет сообщено об этой ошибке.\n" \
                               "Чтобы начать общение заново, воспользуйтесь командой /start."
