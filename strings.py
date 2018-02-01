# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})
# TODO: maybe add a preformat to all strings in this file

# Currency symbol
currency_symbol = "€"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} disponibili"

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Ciao!\n" \
                           "Benvenuto su greed!"

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Cosa vorresti fare?"

# Conversation: the same message as above but when the first has already been sent
conversation_open_user_menu_multiple = "Hai bisogno di qualcos'altro?"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Sei un amministratore di greed!\n" \
                               "Cosa vorresti fare?"

# Conversation: select a payment method
conversation_payment_method = "Come vuoi aggiungere fondi al tuo portafoglio?"

# Conversation: select a product to edit
conversation_admin_select_product = "Che prodotto vuoi modificare?"

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

# Admin menu: go to user mode
menu_user_mode = "👤 Passa alla modalità utente"

# Admin menu: add product
menu_add_product = "✨ Nuovo prodotto"

# Menu: cancel
menu_cancel = "🔙 Annulla"

# Add product: name?
ask_product_name = "Come si deve chiamare il prodotto?"

# Add product: description?
ask_product_description = "Quale deve essere la descrizione del prodotto?"

# Add product: price?
ask_product_price = "Quanto deve costare il prodotto?\n" \
                    "Scrivi <code>skip</code> se vuoi che il prodotto non sia ancora in vendita."

# Add product: image?
ask_product_image = "Che immagine vuoi che abbia il prodotto?"

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

# Info: informazioni sul bot
bot_info = 'Questo bot utilizza <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' un framework di @Steffo per i pagamenti su Telegram rilasciato sotto la' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE">Affero General Public License 3.0</a>.\n' \
           'Il codice sorgente di questa versione è disponibile <i>qui</i>.\n'

# Success: product has been added to the database
success_product_added = "✅ Il prodotto è stato aggiunto con successo!"

# Success: product has been added to the database
success_product_edited = "✅ Il prodotto è stato modificato con successo!"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Questo bot funziona solo in chat private."

# Error: a message was sent in a chat, but no worker exists for that chat. Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ La conversazione con il bot è interrotta.\n" \
                           "Per riavviarla, manda il comando /start al bot."

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ Il massimo di fondi che possono essere aggiunti in una singola transazione è {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Il minimo di fondi che possono essere aggiunti in una singola transazione è {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Questo pagamento è scaduto ed è stato annullato. Se vuoi ancora aggiungere fondi, usa l'opzione Aggiungi fondi del menu."

# Error: a product with that name already exists
error_duplicate_name = "️⚠ Esiste già un prodotto con questo nome."


