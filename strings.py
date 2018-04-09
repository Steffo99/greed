# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})
# TODO: maybe add a preformat to all strings in this file

# Currency symbol
currency_symbol = "€"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} disponibili"

# Copies of a product in cart
in_cart_format_string = "{quantity} nel carrello"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{stock}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Ordine #{id}"

# Order info displayed string
order_format_string = "di {user}\n" \
                      "{value}\n" \
                      "Creato {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "\n" \
                      "{notes}"

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Ciao!\n" \
                           "Benvenuto su greed!"

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Cosa vorresti fare?\n" \
                              "Hai <b>{credit}</b> sul portafoglio."

# Conversation: the same message as above but when the first has already been sent
conversation_open_user_menu_multiple = "Hai bisogno di qualcos'altro?"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Sei un amministratore di greed!\n" \
                               "Cosa vorresti fare?"

# Conversation: select a payment method
conversation_payment_method = "Come vuoi aggiungere fondi al tuo portafoglio?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Che prodotto vuoi modificare?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Che prodotto vuoi eliminare?"

# Conversation: add extra notes to the order
conversation_extra_notes = "Che messaggio vuoi lasciare insieme al tuo ordine?"

# Conversation: click below to pay for the purchase
conversation_cart_actions = "Quando hai finito di aggiungere prodotti al carrello, clicca uno dei pulsanti qui sotto!"

# Conversation: confirm the cart contents
conversation_confirm_cart = "Il tuo carrello contiene questi prodotti:\n" \
                            "{product_list}" \
                            "\n" \
                            "Totale: {total_cost}\n" \
                            "Procedere?"

# Conversation: the user activated the live orders mode
conversation_live_orders_start = "Hai avviato la modalità Ordini Live!\n" \
                                 "Per interrompere il flusso di ordini, manda un qualsiasi messaggio in chat."

# Notification: the conversation has expired
conversation_expired = "🕐 Il bot non ha ricevuto messaggi per un po' di tempo, quindi ha chiuso la conversazione.\n" \
                       "Per riavviarne una nuova, invia il comando /start."

# User menu: order
menu_order = "🛍 Ordina"

# User menu: order status
menu_order_status = "❓ Stato ordini"

# User menu: add credit
menu_add_credit = "💵 Aggiungi fondi"

# User menu: bot info
menu_bot_info = "ℹ️ Informazioni sul bot"

# User menu: cash
menu_cash = "💵 In contanti"

# User menu: credit card
menu_credit_card = "💳 Con una carta di credito"

# Admin menu: products
menu_products = "📝️ Prodotti"

# Admin menu: orders
menu_orders = "📦 Ordini"

# Menu: transactions
menu_transactions = "💳 Transazioni"

# Admin menu: go to user mode
menu_user_mode = "👤 Passa alla modalità utente"

# Admin menu: add product
menu_add_product = "✨ Nuovo prodotto"

# Admin menu: delete product
menu_delete_product = "❌ Elimina prodotto"

# Menu: cancel
menu_cancel = "🔙 Annulla"

# Menu: skip
menu_skip = "⏭ Salta"

# Menu: done
menu_done = "✅️ Fatto"

# Menu: pay invoice
menu_pay = "💳 Paga"

# Menu: complete
menu_complete = "✅ Completa"

# Menu: refund
menu_refund = "✴️ Rimborsa"

# Menu: stop
menu_stop = "🛑 Interrompi"

# Menu: add to cart
menu_add_to_cart = "➕ Aggiungi"

# Menu: remove from cart
menu_remove_from_cart = "➖ Rimuovi"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣ "

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Add product: name?
ask_product_name = "Come si deve chiamare il prodotto?"

# Add product: description?
ask_product_description = "Quale deve essere la descrizione del prodotto?"

# Add product: price?
ask_product_price = "Quanto deve costare il prodotto?\n" \
                    "Scrivi <code>X</code> se vuoi che il prodotto non sia ancora in vendita."

# Add product: image?
ask_product_image = "Che immagine vuoi che abbia il prodotto?"

# Order product: notes?
ask_order_notes = "Vuoi lasciare un messaggio insieme all'ordine?\n" \
                  "Sarà visibile al negoziante."

# Refund product: reason?
ask_refund_reason = "Allega una motivazione a questo rimborso.\n" \
                    "Sarà visibile al cliente."

# Thread has started downloading an image and might be unresponsive
downloading_image = "Sto scaricando la tua foto!\n" \
                    "Potrei metterci un po'... Abbi pazienza!\n" \
                    "Non sarò in grado di risponderti durante il download."

# Edit product: current value
edit_current_value = "Il valore attuale è:\n" \
                     "<pre>{value}</pre>"

# Payment: cash payment info
payment_cash = "Puoi pagare in contanti alla sede fisica del negozio.\n" \
               "Il gestore provvederà ad aggiungere credito al tuo account appena gli avrai consegnato i soldi."

# Payment: invoice amount
payment_cc_amount = "Quanti fondi vuoi aggiungere al tuo portafoglio?"

# Payment: add funds invoice title
payment_invoice_title = "Aggiunta di fondi"

# Payment: add funds invoice description
payment_invoice_description = "Pagando questa ricevuta verranno aggiunti {amount} al portafoglio."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Ricarica"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Supplemento carta"

# Notification: order has been placed
notification_order_placed = "E' stato piazzato un nuovo ordine:\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Un tuo ordine è stato completato!\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Un tuo ordine è stato rimborsato!\n" \
                              "{order}"

# Refund reason
refund_reason = "Motivazione del rimborso:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'Questo bot utilizza <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' un framework di @Steffo per i pagamenti su Telegram rilasciato sotto la' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE">Affero General Public License 3.0</a>.\n' \
           'Il codice sorgente di questa versione è disponibile <i>qui</i>.\n'

# Success: product has been added/edited to the database
success_product_edited = "✅ Il prodotto è stato aggiunto/modificato con successo!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Il prodotto è stato eliminato con successo!"

# Success: order has been created
success_order_created = "✅ L'ordine è stato inviato con successo!"

# Success: order was marked as completed
success_order_completed = "✅ Hai segnato l'ordine #{order_id} come completato."

# Success: order was refunded successfully
success_order_refunded = "✴️ L'ordine #{order_id} è stato rimborsato con successo."

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Questo bot funziona solo in chat private."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ La conversazione con il bot è interrotta.\n" \
                           "Per riavviarla, manda il comando /start al bot."

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ Il massimo di fondi che possono essere aggiunti in una singola transazione è " \
                                "{max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Il minimo di fondi che possono essere aggiunti in una singola transazione è " \
                                 "{min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Questo pagamento è scaduto ed è stato annullato. Se vuoi ancora aggiungere fondi, " \
                        "usa l'opzione Aggiungi fondi del menu. "

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Esiste già un prodotto con questo nome."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ Non hai credito sufficiente per effettuare l'ordine."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Questo ordine è già stato processato."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  Non hai ancora piazzato ordini, quindi non c'è niente da visualizzare!"
