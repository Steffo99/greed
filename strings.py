# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})
# Current localization is Italian

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
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "<b>Ordine #{id}</b>"

# Order info string, shown to the admins
order_format_string = "di {user}\n" \
                      "Creato {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTALE: <b>{value}</b>\n" \
                      "\n" \
                      "Note del cliente: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Ordine {status_text}</b>\n" \
                           "{items}\n" \
                           "TOTALE: <b>{value}</b>\n" \
                           "\n" \
                           "Note: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Caricamento delle transazioni in corso...\n" \
                       "Attendi qualche secondo, per piacere.</i>"

# Transactions page
transactions_page = "Pagina <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "E' stato generato un file .csv contenente tutte le transazioni archiviate nel database del bot.\n" \
              "E' possibile aprire questo file con altri programmi, come ad esempio LibreOffice Calc, per elaborare" \
              " i dati."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Ciao!\n" \
                           "Benvenuto su greed!\n" \
                           "Quella che vedi qui è la versione <b>Alpha</b> del software.\n" \
                           "Pertanto, funzioni potranno essere aggiunte o rimosse in qualsiasi momento," \
                           " e l'interfaccia utente potrebbe essere incompleta."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Cosa vorresti fare?\n" \
                              "Hai <b>{credit}</b> sul portafoglio.\n" \
                              "\n" \
                              "<i>Per selezionare un'operazione, premi un tasto nella tastiera in basso.\n" \
                              "Se la tastiera non si è aperta, puoi aprirla premendo il tasto con quattro quadratini" \
                              " nella barra dei messaggi.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Sei un <b>amministratore</b> di greed!\n" \
                               "Cosa vorresti fare?\n" \
                               "\n" \
                               "<i>Per selezionare un'operazione, premi un tasto nella tastiera in basso.\n" \
                               "Se la tastiera non si è aperta, puoi aprirla premendo il tasto con quattro quadratini" \
                               " nella barra dei messaggi.</i>"

# Conversation: select a payment method
conversation_payment_method = "Come vuoi aggiungere fondi al tuo portafoglio?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Che prodotto vuoi modificare?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Che prodotto vuoi eliminare?"

# Conversation: select a user to edit
conversation_admin_select_user = "Seleziona l'utente a cui vuoi aggiungere o togliere credito."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Aggiungi prodotti al carrello scorrendo in su e premendo il pulsante Aggiungi sotto" \
                            " i prodotti che desideri acquistare. Quando avrai terminato, torna a questo messaggio e" \
                            " premi il tasto Conferma.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "Il tuo carrello contiene questi prodotti:\n" \
                            "{product_list}" \
                            "Totale: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Se vuoi procedere, premi il tasto Conferma sotto a questo messaggio.\n" \
                            "Per annullare, premi il tasto Annulla.</i>"

# Conversation: the user activated the live orders mode
conversation_live_orders_start = "Sei in modalità di <b>Ricezione Ordini</b>!\n" \
                                 "Tutti i nuovi ordini piazzati dai clienti ti appariranno in tempo reale in questa" \
                                 " chat, e potrai segnarli come completati oppure rimborsare il credito al cliente.\n" \
                                 "\n" \
                                 "<i>Premi il tasto Interrompi sotto a questo messaggio per interrompere la" \
                                 " ricezione.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Che tipo di assistenza desideri ricevere?"

# Notification: the conversation has expired
conversation_expired = "🕐 Non ho ricevuto messaggi da un po' di tempo, quindi per risparmiare energia" \
                       " ho chiuso la conversazione.\n" \
                       "Se vuoi avviarne una nuova, invia di nuovo il comando /start."

# User menu: order
menu_order = "🛒 Ordina"

# User menu: order status
menu_order_status = "🛍 I miei ordini"

# User menu: add credit
menu_add_credit = "💵 Aggiungi fondi"

# User menu: bot info
menu_bot_info = "ℹ️ Info sul bot"

# User menu: cash
menu_cash = "💵 In contanti"

# User menu: credit card
menu_credit_card = "💳 Con una carta di credito"

# Admin menu: products
menu_products = "📝️ Prodotti"

# Admin menu: orders
menu_orders = "📦 Ordini"

# Menu: transactions
menu_transactions = "💳 Elenco transazioni"

# Menu: edit credit
menu_edit_credit = "💰 Crea transazione"

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

# Menu: help menu
menu_help = "❓ Aiuto e assistenza"

# Menu: guide
menu_guide = "📖 Guida"

# Menu: next page
menu_next = "▶️ Avanti"

# Menu: previous page
menu_previous = "◀️ Indietro"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Contatta il negozio"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

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
text_not_processed = "in sospeso"

# Text: completed order
text_completed = "completato"

# Text: refunded order
text_refunded = "rimborsato"

# Add product: name?
ask_product_name = "Come si deve chiamare il prodotto?"

# Add product: description?
ask_product_description = "Quale deve essere la descrizione del prodotto?"

# Add product: price?
ask_product_price = "Quanto deve costare il prodotto?\n" \
                    "Scrivi <code>X</code> se vuoi che il prodotto non sia ancora in vendita."

# Add product: image?
ask_product_image = "Che immagine vuoi che abbia il prodotto?\n" \
                    "\n" \
                    "<i>Invia la foto, o se preferisci lasciare il prodotto senza immagine premi il tasto Salta qui" \
                    " sotto.</i>"

# Order product: notes?
ask_order_notes = "Vuoi lasciare una nota insieme all'ordine?\n" \
                  "Sarà visibile agli addetti del negozio.\n" \
                  "\n" \
                  "<i>Invia un messaggio con la nota che vuoi lasciare, oppure premi il pulsante Salta sotto a questo" \
                  " messaggio per non lasciare nulla.</i>"

# Refund product: reason?
ask_refund_reason = "Allega una motivazione a questo rimborso.\n" \
                    "Sarà visibile al cliente."

# Edit credit: notes?
ask_transaction_notes = "Allega una nota a questa transazione.\n" \
                        "Sarà visibile al cliente in seguito all'accredito / addebito e nel registro delle transazioni."

# Edit credit: amount?
ask_credit = "Di quanto vuoi modificare il credito del cliente?\n" \
             "\n" \
             "<i>Invia un messaggio contenente l'importo.\n" \
             "Metti un segno </i><code>+</code><i> se vuoi aggiungere credito all'account del cliente," \
             " oppure un segno </i><code>-</code><i> se vuoi dedurlo.</i>"

# Edit admin: can edit products?
ask_edit_products = "Vuoi che l'amministratore sia autorizzato a modificare la configurazione dei prodotti?"

# Edit admin: can receive orders?
ask_receive_orders = "Vuoi che l'amministratore sia autorizzato a ricevere e gestire gli ordini?"

# Edit admin: can create transactions?
ask_create_transactions = "Vuoi che l'amministratore sia autorizzato a creare nuove transazioni?"

# Edit admin: should be displayed on help
ask_display_on_help = "Vuoi che l'amministratore venga visualizzato nella sezione Contatta il negozio?"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Sto scaricando la tua foto!\n" \
                    "Potrei metterci un po'... Abbi pazienza!\n" \
                    "Non sarò in grado di risponderti durante il download."

# Edit product: current value
edit_current_value = "Il valore attuale è:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Premi il tasto Salta sotto questo messaggio per mantenere lo stesso valore.</i>"

# Payment: cash payment info
payment_cash = "Puoi pagare in contanti alla sede fisica del negozio.\n" \
               "Paga alla cassa, e fornisci al gestore del negozio questo id:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "Quanti fondi vuoi aggiungere al tuo portafoglio?\n" \
                    "\n" \
                    "<i>Seleziona un importo con i bottoni sotto, oppure inseriscilo manualmente con la tastiera" \
                    " normale.</i>"

# Payment: add funds invoice title
payment_invoice_title = "Aggiunta di fondi"

# Payment: add funds invoice description
payment_invoice_description = "Pagando questa ricevuta verranno aggiunti {amount} al portafoglio.\n\n" \
                              "Visto che sei nella versione Alpha del software, puoi effettuare pagamenti infiniti" \
                              " con la carta di credito di prova `4242 4242 4242 4242`," \
                              " con qualsiasi CVV e una qualsiasi data di scadenza valida."

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

# Notification: a manual transaction was applied
notification_transaction_created = "E' stata applicata una nuova transazione al tuo portafoglio:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Motivazione del rimborso:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'Questo bot utilizza <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' un framework di @Steffo per i pagamenti su Telegram rilasciato sotto la' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE">Affero General Public License 3.0</a>.\n' \
           'Il codice sorgente di questa versione è disponibile <i>qui</i>.\n'

# Help: guide
help_msg = "La guida del bot non è ancora disponibile.\n" \
           "Riprova più avanti!"

# Help: contact shopkeeper
contact_shopkeeper = "Attualmente, il personale disponibile ad offrire assistenza agli utenti è composto da:\n" \
                     "{shopkeepers}\n" \
                     "<i>Clicca / Tocca uno dei loro nomi per contattarli in una chat di Telegram.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Il prodotto è stato aggiunto/modificato con successo!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Il prodotto è stato eliminato con successo!"

# Success: order has been created
success_order_created = "✅ L'ordine è stato inviato con successo!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Hai segnato l'ordine #{order_id} come completato."

# Success: order was refunded successfully
success_order_refunded = "✴️ L'ordine #{order_id} è stato rimborsato con successo."

# Success: transaction was created successfully
success_transaction_created = "✅ La transazione è stata creata con successo!\n" \
                              "{transaction}"

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
error_no_orders = "⚠️  Non hai ancora piazzato ordini, quindi non c'è niente da visualizzare."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  L'utente selezionato non esiste."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh no! Un <b>errore</b> ha interrotto questa conversazione.\n" \
                               "L'errore è stato segnalato allo sviluppatore di greed in modo che possa sistemarlo.\n" \
                               "Per avviare una nuova conversazione, invia il comando /start."