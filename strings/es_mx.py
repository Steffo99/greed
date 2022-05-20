# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Currency symbol
currency_symbol = "$"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} disponible(s)"

# Copies of a product in cart
in_cart_format_string = "{quantity} en el carrito"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Orden #{id}"

# Order info string, shown to the admins
order_format_string = "por {user}\n" \
                      "Creado en {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTAL: <b>{value}</b>\n" \
                      "\n" \
                      "Notas del Cliente: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Orden {status_text}</b>\n" \
                           "{items}\n" \
                           "TOTAL: <b>{value}</b>\n" \
                           "\n" \
                           "Notas: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Cargando transacciones...\n" \
                       "Por favor espera unos segundos.</i>"

# Transactions page
transactions_page = "Página <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "Un archivo 📄 .csv file que contiene todas las transacciones almacenadas en la base de datos del bot fue generado.\n" \
              "Puedes abrir este archivo con otros programas, como LibreOffice Calc, para procesar los datos."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "¡Hola!\n" \
                           "¡Bienvenido a greed!\n" \
                           "Esta es la versión 🅱️ <b>Beta</b> del software.\n" \
                           "Es completamente utilizable, pero puede haber algunos errores todavía presentes.\n" \
                           "Si encuentras alguno, por favor repórtalo en https://github.com/Steffo99/greed/issues."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "¿Qué te gustaría hacer?\n" \
                              "💰 Tienes <b>{credit}</b> en tu billetera.\n" \
                              "\n" \
                              "<i>Selecciona una opción en el menú de opciones para iniciar una operación.\n" \
                              "Si el menú no se ha desplegado, puedes abrirlo presionando el botón de" \
                              " los cuatro cuadrados pequeños en la barra de mensajes.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "¡Eres 💼 <b>Administrador</b> de esta tienda!\n" \
                               "¿Que te gustaría hacer?\n" \
                               "\n" \
                               "<i>Selecciona una opción en el menú de opciones para iniciar una operación.\n" \
                               "Si el menú no se ha desplegado, puedes abrirlo presionando el botón de" \
                               " los cuatro cuadrados pequeños en la barra de mensajes.</i>"

# Conversation: select a payment method
conversation_payment_method = "¿Cómo quieres agregar fondos a tu cartera?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ ¿Qué producto quieres editar?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ ¿Qué producto quieres eliminar?"

# Conversation: select a user to edit
conversation_admin_select_user = "Selecciona un usuario para editar."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Agrega productos al carrito desplazándote hacia arriba y presionando el botón <b>Agregar</b>" \
                            " debajo del producto que quieres agregar. Cuando termines, vuelve a este mensaje y presiona" \
                            " el botón <b>Listo</b> debajo de este mensaje.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Tu carrito contiene los siguientes productos:\n" \
                            "{product_list}" \
                            "Total: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Si quieres proceder con la compra, presiona el botón <b>Listo</b> debajo de este mensaje.\n" \
                            "Para cancelar, presiona el botón <b>Cancelar</b>.</i>"

# Live orders mode: start
conversation_live_orders_start = "Estás en el modo <b>Órdenes en vivo</b>\n" \
                                 "Todos las nuevas órdenes realizadas por los clientes aparecerán en tiempo real en este chat y podrás" \
                                 " marcarlas como ✅ Completada" \
                                 " o ✴️ Reembolsar el crédito al cliente."

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Presiona el botón <b>Detener</b> debajo de este mensaje para detener las" \
                                " órdenes en vivo.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "¿Qué tipo de ayuda necesitas?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "¿Estás seguro de que quieres promover este usuario a 💼 Administrador?\n" \
                                       "¡Es una acción irreversible!"

# Conversation: language select menu header
conversation_language_select = "Selecciona un idioma:"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Estás cambiando a 👤 Modo Cliente.\n" \
                                   "Si quieres volver al menú de 💼 Administrador, reinicia la conversación con el comando /start."

# Notification: the conversation has expired
conversation_expired = "🕐  No he recibido ningún mensaje en un tiempo, así que cerraré la conversación para ahorrar" \
                       " recursos.\n" \
                       "Si quieres iniciar una nueva, envía un nuevo comando /start."

# User menu: order
menu_order = "🛒 Ordenar productos"

# User menu: order status
menu_order_status = "🛍 Mis órdenes"

# User menu: add credit
menu_add_credit = "💵 Agregar fondos"

# User menu: bot info
menu_bot_info = "ℹ️ Información del bot"

# User menu: cash
menu_cash = "💵 Con efectivo"

# User menu: credit card
menu_credit_card = "💳 Con tarjeta"

# Admin menu: products
menu_products = "📝️ Productos"

# Admin menu: orders
menu_orders = "📦 Ordenes"

# Menu: transactions
menu_transactions = "💳 Lista de transacciones"

# Menu: edit credit
menu_edit_credit = "💰 Crear transacción"

# Admin menu: go to user mode
menu_user_mode = "👤 Cambiar a modo cliente"

# Admin menu: add product
menu_add_product = "✨ Nuevo producto"

# Admin menu: delete product
menu_delete_product = "❌ Eliminar producto"

# Menu: cancel
menu_cancel = "🔙 Cancelar"

# Menu: skip
menu_skip = "⏭ Omitir"

# Menu: done
menu_done = "✅️ Listo"

# Menu: pay invoice
menu_pay = "💳 Pagar"

# Menu: complete
menu_complete = "✅ Completar"

# Menu: refund
menu_refund = "✴️ Reembolsar"

# Menu: stop
menu_stop = "🛑 Detener"

# Menu: add to cart
menu_add_to_cart = "➕ Agregar"

# Menu: remove from cart
menu_remove_from_cart = "➖ Remover"

# Menu: help menu
menu_help = "❓ Ayuda / Soporte"

# Menu: guide
menu_guide = "📖 Guía"

# Menu: next page
menu_next = "▶️ Siguiente"

# Menu: previous page
menu_previous = "◀️ Anterior"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Contactar con la tienda"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Editar Administradores"

# Menu: language
menu_language = "🇲🇽 Idioma"

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
text_not_processed = "Pendiente"

# Text: completed order
text_completed = "Completada"

# Text: refunded order
text_refunded = "Reembolsada"

# Text: product not for sale
text_not_for_sale = "No para la venta"

# Add product: name?
ask_product_name = "¿Cuál debería ser el nombre del producto?"

# Add product: description?
ask_product_description = "¿Cuál debería ser la descripción del producto?"

# Add product: price?
ask_product_price = "¿Cuál debería ser el precio del producto?\n" \
                    "Ingresa una <code>X</code> si quieres que el producto aún no esté a la venta."

# Add product: image?
ask_product_image = "🖼 ¿Qué imagen quieres que tenga el producto?\n" \
                    "\n" \
                    "<i>Envía la foto, u <b>Omite</b> esta fase para no agregar ninguna imagen.</i>"

# Order product: notes?
ask_order_notes = "¿Quieres dejar una nota junto con el pedido?\n" \
                  "💼 Será visible para los Administradores de la tienda.\n" \
                  "\n" \
                  "<i>Envía un mensaje con la nota que quieres dejar o presiona el botón <b>Omitir</b> debajo de este" \
                  " mensaje para no dejar ninguna.</i>"

# Refund product: reason?
ask_refund_reason = " Adjunta un motivo a este reembolso.\n" \
                    "👤  Será visible para el cliente."

# Edit credit: notes?
ask_transaction_notes = " Adjunta una nota a esta transacción.\n" \
                        "👤 Será visible para el cliente al recibir la transacción" \
                        " y para los 💼 Administradores en el registro de transacciones."

# Edit credit: amount?
ask_credit = "¿Cómo quieres cambiar el crédito del cliente?\n" \
             "\n" \
             "<i>Envía un mensaje que contenga la cantidad.\n" \
             "Usa el signo </i><code>+</code><i> para aumentar el crédito de la cuenta del cliente," \
             " o el signo </i><code>-</code><i> para disminuirlo.</i>"

# Header for the edit admin message
admin_properties = "<b>Permisos de {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Editar productos"

# Edit admin: can receive orders?
prop_receive_orders = "Recibir órdenes"

# Edit admin: can create transactions?
prop_create_transactions = "Administrar transacciones"

# Edit admin: show on help message?
prop_display_on_help = "Mostrarlo al cliente como contacto de ayuda"

# Thread has started downloading an image and might be unresponsive
downloading_image = "¡Estoy descargando la imágen!\n" \
                    "Esto podría tomar tiempo... Por favor, se paciente.\n" \
                    "No podré responderte mientras estoy descargando."

# Edit product: current value
edit_current_value = "El valor actual es:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Presione el botón <b>Omitir</b> debajo de este mensaje para mantener el mismo valor.</i>"

# Payment: cash payment info
payment_cash = "Puedes pagar en efectivo en la ubicación física de la tienda.\n" \
               "Paga al finalizar la compra y dale este ID al encargado:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "¿Cuántos fondos quieres agregar a tu cartera?\n" \
                    "\n" \
                    "<i>Selecciona una cantidad con los botones de abajo, o ingrésala manualmente con el teclado</i>"

# Payment: add funds invoice title
payment_invoice_title = "Agregar fondos"

# Payment: add funds invoice description
payment_invoice_description = "Pagar esta factura agregará {amount} a tu cartera."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Recargar"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Comisión de la transacción"

# Notification: order has been placed
notification_order_placed = "Se realizó una nueva orden:\n" \
                            "\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "¡Tu orden ha sido completada!\n" \
                               "\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "¡Tu orden ha sido reembolsada!\n" \
                              "\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Se ha aplicado una nueva transacción a tu cartera:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Motivo del reembolso:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'Este bot está usando <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' un framework creado por @Steffo para pagos a través de Telegram lanzado bajo la licencia:' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public License 3.0</a>.\n'

# Help: guide
help_msg = "La guía de greed está disponible en este enlace:\n" \
           "https://github.com/Steffo99/greed/wiki"

# Help: contact shopkeeper
contact_shopkeeper = "Actualmente, el personal disponible para brindar asistencia al cliente está compuesto por:\n" \
                     "{shopkeepers}\n" \
                     "<i>Haz click o toca uno de sus nombres para contactarlos a través de Telegram.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ ¡El producto se ha agregado/modificado satisfactoriamente!"

# Success: product has been marked as deleted in the database
success_product_deleted = "✅ ¡El producto se ha eliminado satisfactoriamente!"

# Success: order has been created
success_order_created = "✅ ¡La orden se envió satisfactoriamente!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Marcaste la orden #{order_id} como completada."

# Success: order was refunded successfully
success_order_refunded = "✴️ La orden #{order_id} fue reembolsada."

# Success: transaction was created successfully
success_transaction_created = "✅ ¡La transacción se creó satisfactoriamente!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Este bot solo funciona en chats privados."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ La conversación con el bot fue interrumpida.\n" \
                           "Para reiniciarla, envía el comando /start."

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 La conversación con el bot está comenzando.\n" \
                         "Por favor, espera unos momentos antes de enviar más comandos."

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ La cantidad máxima que se puede agregar en una sola transacción es {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ La cantidad mínima que se puede agregar en una sola transacción es {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Esta factura venció y fue cancelada. Si aún quieres agregar fondos, usa la opción." \
                        " <b>Agregar fondos</b> del menú de opciones."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Ya existe un producto con el mismo nombre."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ No tienes suficiente crédito para realizar el pedido."

# Error: order has already been cleared
error_order_already_cleared = "⚠️ Este pedido ya ha sido procesado."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️ Aún no has realizado ninguna orden, no hay nada que mostrar."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️ El usuario seleccionado no existe."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh no! Un <b>error</b> ha interrumpido esta conversación\n" \
                               "El error ha sido reportado al propietario del bot para que pueda solucionarlo.\n" \
                               "Para reiniciar la conversación, envía el comando /start nuevamente."
