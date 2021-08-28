# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Part of the translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "T"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} دردسترس است"

# Copies of a product in cart
in_cart_format_string = "{quantity} در کارت"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "شماره سفارش #{id}"

# Order info string, shown to the admins
order_format_string = "توسط {user}\n" \
                      "ساخته شده در {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "مجموع: <b>{value}</b>\n" \
                      "\n" \
                      "توضیحات مشتری: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>سفارش {status_text}</b>\n" \
                           "{items}\n" \
                           "مجموع: <b>{value}</b>\n" \
                           "\n" \
                           "توضیحات: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>سفارش در حال انجام است...\n" \
                       "لطفا چند ثانیه صبر کنید.</i>"

# Transactions page
transactions_page = "صفحه <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "A 📄 .csv file containing all transactions stored in the bot database was generated.\n" \
              "You can open this file with other programs, such as LibreOffice Calc, to process" \
              " the data."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "سلام!\n" \
                           "خوش مدید!\n" \
                           "این یک نسخه آزمایشی است.\n"

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "چه چیزی نیاز دارید?\n" \
                              "💰 شما <b>{credit}</b> در کیف پول خو دارید.\n" \
                              "\n" \
                              "<i>یکی از کلید های زیر را انتخاب کنید.\n"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "شما 💼 <b>Manager</b> مدیر فروشگاه هستید!\n" \
                               "چه چیزی نیاز دارید?\n" \
                               "\n" \
                               "<i>یکی از کلید های زیر را انتخاب کنید.\n"

# Conversation: select a payment method
conversation_payment_method = "چه مقدار مبلغ میخاین به کیف پولتون اضافه کنین?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ کدوم محصول رو میخاین ویرایش کنین?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ کدوم محصول رو میخاین حذف کنین?"

# Conversation: select a user to edit
conversation_admin_select_user = "یک کاربر را انتخاب کنید."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Add products to cart by scrolling up and pressing the Add button below" \
                            " the products you want to add to the cart. When you're done, go back to this message and" \
                            " press the Done button below.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Your cart contains the following products:\n" \
                            "{product_list}" \
                            "Total: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>If you want to proceed, press the Done button below this message.\n" \
                            "To cancel, press the Cancel button.</i>"

# Live orders mode: start
conversation_live_orders_start = "You are in <b>Live Orders</b> mode\n" \
                                 "All new orders placed by customers will appear in real time in this chat, and you" \
                                 " will be able to mark them as ✅ Completed" \
                                 " or ✴️ Refund the credit to the customer."

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Press the Stop button below this message to stop the" \
                                " feed.</i>"

# Conversation: help menu has been openedWhat would you like to do
conversation_open_help_menu = "چه کمکی نیاز دارید?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Are you sure you want to promote this user to 💼 Manager?\n" \
                                       "It is an irreversible action!"

# Conversation: language select menu header
conversation_language_select = "Select a language:"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " You are switching to 👤 Customer mode.\n" \
                                   "If you want to go back to the 💼 Manager menu, restart the conversation with /start."

# Notification: the conversation has expired
conversation_expired = "🕐  I haven't received any messages in a while, so I closed the conversation to save" \
                       " resources.\n" \
                       "If you want to start a new one, send a new /start command."

# User menu: order
menu_order = "🛒 سفارش محصولات"

# User menu: order status
menu_order_status = "🛍 سفارشات من"

# User menu: add credit
menu_add_credit = "💵 اضافه کردن دارایی "

# User menu: bot info
menu_bot_info = "ℹ️ درباره بات"

# User menu: cash
menu_cash = "💵 منو هزینه ها"

# User menu: credit card
menu_credit_card = "💳 با کردیت کارت"

# Admin menu: products
menu_products = "📝️ محصولات"

# Admin menu: orders
menu_orders = "📦 سفارشات"

# Menu: transactions
menu_transactions = "💳 لیست تراکنش ها"

# Menu: edit credit
menu_edit_credit = "💰 ایجاد تراکنش"

# Admin menu: go to user mode
menu_user_mode = "👤 تغییر به پنل مشتری"

# Admin menu: add product
menu_add_product = "✨ محصول جدید"

# Admin menu: delete product
menu_delete_product = "❌ حذف محصول"

# Menu: cancel
menu_cancel = "🔙 لغو"

# Menu: skip
menu_skip = "⏭ رد"

# Menu: done
menu_done = "✅️ انجام شد"

# Menu: pay invoice
menu_pay = "💳 منو پرداخت"

# Menu: complete
menu_complete = "✅ اتمام"

# Menu: refund
menu_refund = "✴️ برگشت"

# Menu: stop
menu_stop = "🛑 توقف"

# Menu: add to cart
menu_add_to_cart = "➕ اضافه کردن"

# Menu: remove from cart
menu_remove_from_cart = "➖ حذف کردن"

# Menu: help menu
menu_help = "❓ پشتیبانی"

# Menu: guide
menu_guide = "📖 راهنمایی"

# Menu: next page
menu_next = "▶️ بعدی"

# Menu: previous page
menu_previous = "◀️ قبلی"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 ارتباط با فروشگاه"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 ویرایش مدیران"

# Menu: language
menu_language = "🇬🇧 زبان"

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
text_not_processed = "در انتظار"

# Text: completed order
text_completed = "تمام شده"

# Text: refunded order
text_refunded = "برگشت داده شده"

# Add product: name?
ask_product_name = "اسم محصول?"

# Add product: description?
ask_product_description = "توضیحات محصول?"

# Add product: price?
ask_product_price = "مبلغ محصول?\n" \
                    "دکمه ی اینتر را بزنین اگر فعلا قصد فروشش را ندارید."

# Add product: image?
ask_product_image = "🖼 عکس محصول?\n" \
                    "\n" \
                    "مصحول میتواند بدون عکس هم باشد."

# Order product: notes?
ask_order_notes = "توضیحاتی برای سفارش نیاز دارید?\n" \
                  "💼 این پیام برای مدیران قابل مشاهده می باشد.\n" \
                  "\n" \
                  "میتوانید پیامی ارسال نکنید."

# Refund product: reason?
ask_refund_reason = " دلیل برگشت مبلغ خود را بفرمایید.\n" \
                    "👤  It will be visible to the customer."

# Edit credit: notes?
ask_transaction_notes = " Attach a note to this transaction.\n" \
                        "👤 It will be visible to the customer after crediting / debiting" \
                        " and to 💼 Admins in the transaction log."

# Edit credit: amount?
ask_credit = "How do you want to change the customer's credit?\n" \
             "\n" \
             "<i>Send a message containing the amount.\n" \
             "Use the sign </i><code>+</code><i> to add credit to the customer's account," \
             " and the sign </i><code>-</code><i> to deduce it.</i>"

# Header for the edit admin message
admin_properties = "<b>Permissions of {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Edit products"

# Edit admin: can receive orders?
prop_receive_orders = "Receive orders"

# Edit admin: can create transactions?
prop_create_transactions = "Manage transactions"

# Edit admin: show on help message?
prop_display_on_help = "Show to customer"

# Thread has started downloading an image and might be unresponsive
downloading_image = "I'm downloading your photo!\n" \
                    "It might take a while... Please be patient!\n" \
                    "I won't be able to answer you while I'm downloading."

# Edit product: current value
edit_current_value = "The current value is:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Press the Skip button below this message to keep the same value.</i>"

# Payment: cash payment info
payment_cash = "You can pay in cash at the physical location of the store.\n" \
               "Pay at checkout, and give this id to the manager:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "How many funds do you want to add to your wallet?\n" \
                    "\n" \
                    "<i>Select an amount with the buttons below, or enter it manually with the normal keyboard</i>"

# Payment: add funds invoice title
payment_invoice_title = "Adding funds"

# Payment: add funds invoice description
payment_invoice_description = "Paying this invoice will add {amount} to your wallet."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Reload"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Transaction fee"

# Notification: order has been placed
notification_order_placed = "A new order was placed:\n" \
                            "\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Your order has been completed!\n" \
                               "\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Your order has been refunded!\n" \
                              "\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  A new transaction has been applied to your wallet:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Refund reason:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = """بات توسط hoomanjavan74@gmail.com توسعه داده شده است."""

# Help: guide
help_msg = "این یک بات تستی می باشد و بزودی فعال خواهد شد."

# Help: contact shopkeeper
contact_shopkeeper = "Currently, the staff available to provide user assistance is composed of:\n" \
                     "{shopkeepers}\n" \
                     "<i>Click / Tap one of their names to contact them in a Telegram chat.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ The product has been successfully added/modified!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ The product has been successfully deleted!"

# Success: order has been created
success_order_created = "✅ The order was sent successfully!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ You marked the order #{order_id} as completed."

# Success: order was refunded successfully
success_order_refunded = "✴️ Order #{order_id} was refunded."

# Success: transaction was created successfully
success_transaction_created = "✅ The transaction was successfully created!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ This bot only works in private chats."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ The conversation with the bot was interrupted.\n" \
                           "To restart it, send the /start command to the bot."

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 The conversation with the bot is currently starting.\n" \
                         "Please, wait a few moments before sending more commands!"

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ The maximum amount that can be added in a single transaction is {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ The minimum amount that can be added in a single transaction is {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ This invoice has expired and was canceled. If you still want to add funds, use the Add" \
                        " funds menu option."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ A product with the same name already exists."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ You do not have enough credit to place the order."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  This order has already been processed."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  You haven't placed any order yet, so there is nothing to display."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  The selected user does not exist."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh no! An <b>error</b> interrupted this conversation\n" \
                               "The error was reported to the bot owner so that he can fix it.\n" \
                               "To restart the conversation, send the /start command again."
