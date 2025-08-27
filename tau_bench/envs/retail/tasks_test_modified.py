from tau_bench.types import Task, Action

TASKS_TEST_ = [
    Task(
        annotator="0",
        user_id="b63",
        instruction="You are User b63 in 19122. You received your order #W2378156 and wish to exchange the mechanical keyboard for a similar one but with clicky switches and the smart thermostat for one compatible with Google Home instead of Apple HomeKit. If there is no keyboard that is clicky, RGB backlight, full size, you would go for no backlight. You want to make sure everything is addressed in one go.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b63",
                    "zip": "19122",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2378156"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1656367028"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4896585277"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W2378156",
                    "item_ids": ["1151293680", "4983901480"],
                    "new_item_ids": ["7706410293", "7747408585"],
                    "payment_method_id": "credit_card_9513926",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b63",
        instruction="You are User b63 in 19122. You received your order #W2378156 and wish to exchange the mechanical keyboard for a similar one but with clicky switches and the smart thermostat for one compatible with Google Home instead of Apple HomeKit. If there is no keyboard that is clicky, RGB backlight, full size, you would rather exchange only the thermostat. You want to make sure everything is addressed in one go.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b63",
                    "zip": "19122",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2378156"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1656367028"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4896585277"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W2378156",
                    "item_ids": ["4983901480"],
                    "new_item_ids": ["7747408585"],
                    "payment_method_id": "credit_card_9513926",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b63",
        instruction="You are User b63 in 19122. You want to know how many tshirt options are available in the online store right now. You want to also return the cleaner, headphone, and smart watch.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b63",
                    "zip": "19122",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6086499569"},
            ),
            Action(
                name="list_all_product_types",
                kwargs={},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b63"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6247578"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9711842"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4776164"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6679257"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2378156"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W2378156",
                    "item_ids": ["4602305039", "4202497723", "9408160950"],
                    "payment_method_id": "credit_card_9513926",
                },
            ),
        ],
        outputs=['10'],
    ),
    Task(
        annotator="0",
        user_id="b63",
        instruction="You are User b63 in 19122. You want to know how many tshirt options are available in the online store right now. You want to modify all your pending small tshirts to purple, same size, same v-neck, and prefer polyester.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b63",
                    "zip": "19122",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6086499569"},
            ),
            Action(
                name="list_all_product_types",
                kwargs={},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b63"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6247578"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9711842"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4776164"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6679257"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2378156"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b63"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4776164",
                    "item_ids": ["8349118980"],
                    "new_item_ids": ["9647292434"],
                    "payment_method_id": "credit_card_9513926",
                },
            ),
        ],
        outputs=['10'],
    ),
    Task(
        annotator="0",
        user_id="b63",
        instruction="You are User b63 in 19122. You want to know how many tshirt options are available in the online store right now. You want to modify all your pending tshirts (i.e., your 2 relevant orders) to purple, s size, same v-neck, and prefer polyester.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b63",
                    "zip": "19122",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6086499569"},
            ),
            Action(
                name="list_all_product_types",
                kwargs={},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b63"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6247578"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9711842"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4776164"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6679257"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2378156"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b63"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W6247578",
                    "item_ids": ["3799046073"],
                    "new_item_ids": ["9647292434"],
                    "payment_method_id": "credit_card_9513926",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4776164",
                    "item_ids": ["8349118980"],
                    "new_item_ids": ["9647292434"],
                    "payment_method_id": "credit_card_9513926",
                },
            ),
        ],
        outputs=['10'],
    ),
    Task(
        annotator="0",
        user_id="m30",
        instruction="You are User m30 (zip code 28236) and you want to exchange the water bottle and the desk lamp. You want to exchange the water bottle to a bigger one, and the desk lamp to a less bright one (prefer battery > USB > AC). If the agent asks for confirmation, only exchange the desk lamp. If the agent asks for confirmation again, do not exchange anything, and return the water bottle instead.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "m30",
                    "zip": "28236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "m30"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6390527"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W6390527",
                    "item_ids": ["8538875209"],
                    "payment_method_id": "paypal_7644869",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m30",
        instruction="You are User m30 (zip code 28236) and you want to exchange the water bottle and the desk lamp. You want to exchange the water bottle to a bigger one, and the desk lamp to a less bright one (prefer battery > USB > AC). If the agent asks for confirmation, only exchange the desk lamp.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "m30",
                    "zip": "28236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "m30"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6390527"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8310926033"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W6390527",
                    "item_ids": ["8384507844"],
                    "new_item_ids": ["7453605304"],
                    "payment_method_id": "paypal_7644869",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m30",
        instruction="You are User m30 (zip code 28236) and you want to exchange the water bottle and the desk lamp. You want to exchange the water bottle to a bigger one, and the desk lamp to a less bright one (prefer AC adapter > battery > USB). If the agent asks for confirmation, only exchange the desk lamp.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "m30",
                    "zip": "28236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "m30"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6390527"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8310926033"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W6390527",
                    "item_ids": ["8384507844"],
                    "new_item_ids": ["1569765161"],
                    "payment_method_id": "paypal_7644869",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m30",
        instruction="You are User m30 (zip code 28236) and you want to exchange the water bottle and the desk lamp. You want to exchange the water bottle to a bigger one, and the desk lamp to a brighter one (prefer battery > USB > AC). If the agent asks for confirmation, only exchange the desk lamp.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "m30",
                    "zip": "28236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "m30"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6390527"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8310926033"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W6390527",
                    "item_ids": ["8384507844"],
                    "new_item_ids": ["9083642334"],
                    "payment_method_id": "paypal_7644869",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m30",
        instruction="You are User m30 (zip code 28236) and you want to exchange the water bottle and the desk lamp. You want to exchange the water bottle to a bigger one, and the desk lamp to a brighter one (prefer AC adapter > battery > USB). If the agent asks for confirmation, only exchange the desk lamp.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "m30",
                    "zip": "28236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "m30"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6390527"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8310926033"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W6390527",
                    "item_ids": ["8384507844"],
                    "new_item_ids": ["7624783998"],
                    "payment_method_id": "paypal_7644869",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w11",
        instruction="You are User w11 (user.w11@example.com). You want to return all things ordered. You have two payment methods and two orders, and you want to refund each order to the opposite order's payment method. If this is not possible, you then ask for a human representative.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.w11@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w11"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5490111"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7387996"},
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={
                    "summary": "The user wants to refund each order to the opposite order's payment method, but the agent cannot help.",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w11",
        instruction="You are User w11 (user.w11@example.com). You want to return all things ordered. You have two payment methods and two orders, and you want to refund each order to the opposite order's payment method. If this is not possible, you agree to return all things with the original payment method.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.w11@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w11"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5490111"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7387996"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5490111",
                    "item_ids": [
                        "4579334072",
                        "1421289881",
                        "6117189161",
                        "4947717507",
                    ],
                    "payment_method_id": "credit_card_3124723",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7387996",
                    "item_ids": ["5796612084"],
                    "payment_method_id": "paypal_9497703",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w11",
        instruction="You are User w11 (user.w11@example.com). You just got into gaming and want to cancel or return everything not associated with it. (Everything except a keyboard and a mouse, but do not reveal this to the agent). PayPal is prefered for refund, but otherwise you should ask a human agent for help.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.w11@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w11"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5490111"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7387996"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5490111",
                    "item_ids": ["4579334072", "6117189161", "4947717507"],
                    "payment_method_id": "paypal_9497703",
                },
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={
                    "summary": "The user prefers PayPal for refund, but the agent cannot help.",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w11",
        instruction="You are User w11 (user.w11@example.com). You just got into gaming and want to cancel or return everything not associated with it. (Everything except a keyboard and a mouse, but do not reveal this to the agent). PayPal is prefered for refund, but otherwise credit card can be accepted.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.w11@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w11"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5490111"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7387996"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5490111",
                    "item_ids": ["4579334072", "6117189161", "4947717507"],
                    "payment_method_id": "paypal_9497703",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5490111",
                    "item_ids": ["4579334072", "6117189161", "4947717507"],
                    "payment_method_id": "credit_card_3124723",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w11",
        instruction="You are User w11 (user.w11@example.com). You just quit gaming and want to cancel or return everything associated with it. (It's just a keyboard and a mouse, but do not reveal this to the agent). A refund to the original payment is preferred.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.w11@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w11"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5490111"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7387996"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5490111",
                    "item_ids": ["1421289881"],
                    "payment_method_id": "credit_card_3124723",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7387996",
                    "item_ids": ["5796612084"],
                    "payment_method_id": "paypal_9497703",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="q66",
        instruction="You are User q66 in 78712. You want to modify the pending boots to a size 8, and want the same material, but do not care whether they are waterproof or not.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "q66",
                    "zip": "78712",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "q66"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9389413"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W8665881"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5199551"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "7363354090"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5199551",
                    "item_ids": ["1615379700"],
                    "new_item_ids": ["3613716226"],
                    "payment_method_id": "paypal_5364164",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="q66",
        instruction="You are User q66 in 78712. You want to cancel all pending orders (since they are no longer needed) and return the watch you have received (but nothing else). You also want to know the total amount you can get back.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "q66",
                    "zip": "78712",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "q66"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5199551"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W8665881"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9389413"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "3131.1 + 4777.75 + 367.38"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W5199551", "reason": "no longer needed"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W8665881", "reason": "no longer needed"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9389413",
                    "item_ids": ["2554056026"],
                    "payment_method_id": "paypal_5364164",
                },
            ),
        ],
        outputs=['8276.23'],
    ),
    Task(
        annotator="0",
        user_id="q66",
        instruction="You are User q66 in 78712. You want to change #W8665881 to be delivered to Suite 641 instead.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "q66",
                    "zip": "78712",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "q66"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5199551"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W8665881"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9389413"},
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W8665881",
                    "address1": "123 Elm Street",
                    "address2": "Suite 641",
                    "city": "Austin",
                    "state": "TX",
                    "country": "USA",
                    "zip": "78712",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="u15",
        instruction="You are User u15 in 80217. You want to return the office chair because it came with some broken pieces. But if the agent asks you to confirm, you say you want to rethink for a while, and then change your mind to exchange for the same item.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u15",
                    "zip": "80217",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "u15"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2890441"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4794339885"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W2890441",
                    "item_ids": ["8069050545"],
                    "new_item_ids": ["8069050545"],
                    "payment_method_id": "credit_card_1061405",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="u15",
        instruction="You are User u15 in 80217. You want to return the water bottle, and exchange the pet bed and office chair to the cheapest versions. Mention the two things together. If you can only do one of the two things, you prefer to do whatever saves you most money, but you want to know the money you can save in both ways.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u15",
                    "zip": "80217",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "u15"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2890441"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W1267569"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "2747247837"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4794339885"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W2890441",
                    "item_ids": ["2366567022"],
                    "payment_method_id": "credit_card_1061405",
                },
            ),
        ],
        outputs=['54.04', '41.64'],
    ),
    Task(
        annotator="0",
        user_id="l64",
        instruction="You are User l64, and you live in Denver, 80280. You just won a lottery, and you want to upgrade all your items to the most expensive options (but make sure the shoe is still the same size). You want to pay the difference with your gift card, but if it is impossible, PayPal is fine.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "l64",
                    "zip": "80280",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "l64"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4967593"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9911714"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8310926033"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1656367028"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6938111410"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "5149340237"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9911714",
                    "item_ids": [
                        "2366567022",
                        "1340995114",
                        "9791469541",
                        "1763705424",
                    ],
                    "new_item_ids": [
                        "4579334072",
                        "1151293680",
                        "4107812777",
                        "2882812427",
                    ],
                    "payment_method_id": "gift_card_4332117",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5733668"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="l64",
        instruction="You are User l64, and you live in Denver, 80280. You want to exchange your shoes to 4107812777, and use your gift card to cover possible charges. But if the agent asks for confirmation, you change your mind and also want to change product 1656367028 to 1421289881. Since you are not familiar with the domain and might confuse product and item ids, ask the agent to figure out the details on their own if needed. You want to know your gift card balance after all these changes.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "l64",
                    "zip": "80280",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "l64"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4967593"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9911714"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5733668"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4107812777"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1421289881"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1656367028"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4107812777"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6938111410"},
            ),
            Action(
                name="calculate",
                kwargs={
                    "expression": "155.33 - 147.05 + 268.77 - 235.13",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9911714",
                    "item_ids": ["9791469541", "1340995114"],
                    "new_item_ids": ["4107812777", "1421289881"],
                    "payment_method_id": "gift_card_4332117",
                },
            ),
        ],
        outputs=['44.08'],
    ),
    Task(
        annotator="0",
        user_id="l64",
        instruction="You are User l64, and you live in Denver, 80280. You want to change your user address and all possible order addresses to be 101 Highway, New York, 10001. You then regret this, and want to change the user address back to the original address.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "l64",
                    "zip": "80280",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "l64",
                    "address1": "101 Highway",
                    "address2": "",
                    "city": "New York",
                    "state": "NY",
                    "country": "USA",
                    "zip": "10001",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4967593"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9911714"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5733668"},
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W9911714",
                    "address1": "101 Highway",
                    "address2": "",
                    "city": "New York",
                    "state": "NY",
                    "country": "USA",
                    "zip": "10001",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "l64",
                    "address1": "667 Highland Drive",
                    "address2": "Suite 865",
                    "city": "Denver",
                    "state": "CO",
                    "country": "USA",
                    "zip": "80280",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="s61",
        instruction="You are User s61, and you live in Seattle, WA, 98193. You want to exchange the helmet for a medium sized, red, high ventilation type, and you want to exchange the luggage set (in another order) to a two-piece black one with soft material. Lastly, you want to modify the grill you just ordered to the same type as the one you already received.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "s61",
                    "zip": "98193",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "s61"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3561391"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6876713"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9609649"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3947049"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "7765186836"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3947049",
                    "item_ids": ["3358616356"],
                    "new_item_ids": ["8573379326"],
                    "payment_method_id": "credit_card_7901829",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "5426915165"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W6876713",
                    "item_ids": ["6301799585"],
                    "new_item_ids": ["8926329222"],
                    "payment_method_id": "credit_card_7901829",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6819683148"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W3561391",
                    "item_ids": ["5946177616"],
                    "new_item_ids": ["7082455361"],
                    "payment_method_id": "credit_card_7901829",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="s61",
        instruction="You are User s61, and you live in Seattle, WA, 98193. You want to cancel the grill, but if the agent asks you to confirm, you regret your choice and want to keep it. You then want to ask which two t-shirts you have ordered in another order, and what materials they are.",
        actions=[
        ],
        outputs=['polyester', 'cotton'],
    ),
    Task(
        annotator="0",
        user_id="i49",
        instruction="You are User i49, and you live in 32286. You have an order sent to Texas by accident, and you want to know the tracking number of the order, and return all items in it except the pet bed. You want the refund to your amex credit card, and if the agent cannot help, transfer to a human. You don't remember the order number.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "i49",
                    "zip": "32286",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "i49"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3792453"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7181492"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5565470"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2575533"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="i49",
        instruction="You are User i49, and you live in 32286. You have an order sent to Texas by accident, and you want to know the tracking number of the order, and return all items in it except the pet bed. You don't remember the order number.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "i49",
                    "zip": "32286",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "i49"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3792453"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7181492"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5565470"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2575533"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5565470",
                    "item_ids": ["7602931732", "9570044148"],
                    "payment_method_id": "paypal_3024827",
                },
            ),
            Action(
                name="transfer_to_human_agents",
                kwargs={
                    "summary": "The user wants to refund to the amex credit card, but the agent cannot help.",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="i49",
        instruction="You are User i49, and you live in 32286. You want to return the hose, backpack, and exchange the hiking boots to the same item, but with waterproofing. Make sure you mention the two requests at the same time, and if the agent can only do one, you prefer the exchange.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "i49",
                    "zip": "32286",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "i49"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3792453"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7181492"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "7363354090"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W7181492",
                    "item_ids": ["8118291112"],
                    "new_item_ids": ["8277474082"],
                    "payment_method_id": "paypal_3024827",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="i49",
        instruction="You are User i49, and you live in 32286. You want to return the skateboard, garden hose, backpack, keyboard, bed, and also cancel the hose you just ordered. If cancelling one item is not possible, forget about it; you'd just want to cancel the hose and nothing else. You want to know how much you can get in total as refund.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "i49",
                    "zip": "32286",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "i49"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3792453"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7181492"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5565470"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2575533"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W3792453",
                    "item_ids": ["4293355847"],
                    "payment_method_id": "paypal_3024827",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7181492",
                    "item_ids": ["5753502325", "9851293632"],
                    "payment_method_id": "paypal_3024827",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5565470",
                    "item_ids": ["9570044148", "6857426243"],
                    "payment_method_id": "paypal_3024827",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2575533"},
            ),
            Action(
                name="calculate",
                kwargs={
                    "expression": "200.8 + 96.35 + 193.38 + 231.37 + 196.53",
                },
            ),
        ],
        outputs=['918.43'],
    ),
    Task(
        annotator="0",
        user_id="i49",
        instruction="You are User i49, and you live in 32286. You want to exchange your skateboard for a shorter bamboo material one. If several options are available, you want to know all options and their prices, and choose the most expensive one because you believe price is quality. Also, you want to exchange the garden hose you received to the type that you just ordered (pending).",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "i49",
                    "zip": "32286",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "i49"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3792453"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1968349452"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3792453",
                    "item_ids": ["4293355847"],
                    "new_item_ids": ["8176740019"],
                    "payment_method_id": "paypal_3024827",
                },
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W7181492",
                    "item_ids": ["5753502325"],
                    "new_item_ids": ["5206946487"],
                    "payment_method_id": "paypal_3024827",
                },
            ),
        ],
        outputs=['180.1', '189.57', '208.6'],
    ),
    Task(
        annotator="0",
        user_id="w57",
        instruction="You are User w57, and you live in Texas in 76171. You just received your tablet and it is damaged when you opened the package. You want to know the tracking number of the order. Also if the agent can help you exchange or return the tablet (you prefer to exchange for the same item, but if it is not available just return). If the tablet is returned, also cancel the charger you just bought, because it goes with the tablet. Return the sneaker as well.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "w57",
                    "zip": "76171",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w57"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9319364"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9373487"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2692684"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8024098596"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W2692684",
                    "item_ids": ["3788616824"],
                    "payment_method_id": "gift_card_7711863",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9373487"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W9373487", "reason": "no longer needed"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2692684"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5481803"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7449508"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7449508",
                    "item_ids": ["6477915553"],
                    "payment_method_id": "gift_card_7711863",
                },
            ),
        ],
        outputs=['746342064230'],
    ),
    Task(
        annotator="0",
        user_id="w57",
        instruction="You are User w57, and you live in Texas in 76171. You just lost your tablet that you just received. You want to know the tracking number of the order, and if the agent can help you refund or reorder the tablet. You know it's a long shot, but you want to try. If not, cancel the charger you just bought because it goes with the tablet. Also cancel the boot and keep the kettle (if this is not possible, do not do anything about that order), and return the sneaker.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "w57",
                    "zip": "76171",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w57"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9319364"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9373487"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2692684"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5481803"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7449508"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9373487"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W9373487", "reason": "no longer needed"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5481803"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7449508"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7449508",
                    "item_ids": ["6477915553"],
                    "payment_method_id": "gift_card_7711863",
                },
            ),
        ],
        outputs=['746342064230'],
    ),
    Task(
        annotator="0",
        user_id="w57",
        instruction="You are User w57, and you live in Texas in 76171. You just lost your tablet that you just received. You want to know the tracking number of the order, and if the agent can help you refund or reorder the tablet. (You know it's a long shot, but you want to try). If not, cancel the charger you just bought, because it goes with the tablet. Also cancel the boot and kettle, and return the sneaker.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "w57",
                    "zip": "76171",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w57"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9319364"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9373487"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2692684"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5481803"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7449508"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9373487"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W9373487", "reason": "no longer needed"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5481803"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W5481803", "reason": "no longer needed"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7449508"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7449508",
                    "item_ids": ["6477915553"],
                    "payment_method_id": "gift_card_7711863",
                },
            ),
        ],
        outputs=['746342064230'],
    ),
    Task(
        annotator="0",
        user_id="g32",
        instruction="You are User g32, living in the Big Apple in 10108. You had a work-from-home situation and ordered three home office items along with some hiking items, so that you can go back to your parent's place at Seattle to do remote work and enjoy outdoor life. However, your company just announced that you will be back to the office soon. If cancelling partial items is possible with the agent, you want to return the office items (your forgot what) and keep the hiking items. You want to know the total amount you will get back, and you want to get the refund on your original payment method. If cancelling partial items is not possible, just keep the order, but change your default user profile address to the Seattle parent house shown in your order (you do not want to reveal this in the chat).",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "g32",
                    "zip": "10108",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "g32"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6111398"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7043598"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W1845024"},
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "g32",
                    "address1": "517 Lakeview Drive",
                    "address2": "Suite 183",
                    "city": "Seattle",
                    "country": "USA",
                    "state": "WA",
                    "zip": "98195",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="g32",
        instruction="You are User g32, living in the Big Apple in 10108. You had a work-from-home situation and ordered three home office items along with some hiking items, so that you can go back to your parent's place at Seattle to do remote work and enjoy outdoor life. However, your company just announced that you will be back to the office soon. If cancelling partial items is possible with the agent, you want to return the office items (your forgot what) and keep the hiking items. You want to know the total amount you will get back, and you want to get the refund on your original payment method. If cancelling partial items is not possible, just change the address to your NYC place and you will return the items later.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "g32",
                    "zip": "10108",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "g32"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6111398"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7043598"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W1845024"},
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W1845024",
                    "address1": "224 Elm Street",
                    "address2": "Suite 491",
                    "city": "New York",
                    "country": "USA",
                    "state": "NY",
                    "zip": "10108",
                },
            ),
        ],
        outputs=['1093.34'],
    ),
    Task(
        annotator="0",
        user_id="w12",
        instruction="You are User w12 with the email address user.w12@example.com. You want to return the speaker that is more expensive and not resistent to water. Also, you want to modify the 17-inch laptop to the 13-inch version in another order. If no exact item is available, you want to know all available 13-inch options. You prefer i5 over i7, and prefer silver and black than other colors.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.w12@example.com"},
            ),
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.w12@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "w12"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9672333"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4760268021"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W8528674",
                    "item_ids": ["6704763132"],
                    "payment_method_id": "paypal_7664977",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9672333",
                    "item_ids": ["1684786391"],
                    "new_item_ids": ["5052031638"],
                    "payment_method_id": "paypal_7664977",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="u52",
        instruction="Your name is User u52, and you live in 46236. Your email is user.u52@example.com. You just placed an order but you realize that your card has only $1131 credit left, and the order total is more than $1160. You wonder if the agent can help split the payment with another card. If not, you wonder what the most expensive item is and its price, and if you can just cancel that item. If not, you wonder if you can switch all items to their cheapest options and bring the cost down to $1131. If so, do it. If not, you wonder if the agent can just cancel the order so that you can order again.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.u52@example.com"},
            ),
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u52",
                    "zip": "46236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "u52"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9348897"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "3377618313"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9743693396"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "2524789262"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9348897",
                    "item_ids": ["6117189161", "7453605304", "3799046073"],
                    "new_item_ids": ["6700049080", "5320792178", "3234800602"],
                    "payment_method_id": "credit_card_8853416",
                },
            ),
        ],
        outputs=['camera', '481.5'],
    ),
    Task(
        annotator="0",
        user_id="u52",
        instruction="Your name is User u52, and you live in 46236, your email is user.u52@example.com. You just placed an order but you realize that your card has only $1150 credit left, but the order total is more than $1160. You wonder if the agent can help split the payment with another card. If not, you wonder what the most expensive item is and its price, and if you can just cancel that item. If not, you wonder if you can switch all items to their cheapest options and bring the cost down to $1150. If so, do it. If not, you wonder if the agent can just cancel the order so that you can order again.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.u52@example.com"},
            ),
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u52",
                    "zip": "46236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "u52"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9348897"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "3377618313"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9743693396"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "2524789262"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9348897",
                    "item_ids": ["6117189161", "7453605304", "3799046073"],
                    "new_item_ids": ["6700049080", "5320792178", "3234800602"],
                    "payment_method_id": "credit_card_8853416",
                },
            ),
        ],
        outputs=['camera', '481.5'],
    ),
    Task(
        annotator="0",
        user_id="u52",
        instruction="Your name is User u52, and you live in 46236, your email is user.u52@example.com. You just placed an order but you realize that your card has only $950 credit left, but the order total is more than $1100. You wonder if the agent can help split the payment with another card. If not, you wonder what the most expensive item is and its price, and if you can just cancel that item. If not, you wonder if you can switch all items to their cheapest options and bring the cost down to $950. If not, you wonder if the agent can just cancel the order so that you can order again.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.u52@example.com"},
            ),
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u52",
                    "zip": "46236",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "u52"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9348897"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "3377618313"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9743693396"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "2524789262"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
            Action(
                name="calculate",
                kwargs={
                    "expression": "466.75 + 288.82 + 135.24 + 193.38 + 46.66",
                },
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W9348897", "reason": "no longer needed"},
            ),
        ],
        outputs=['camera', '481.5'],
    ),
    Task(
        annotator="0",
        user_id="u78",
        instruction="You are User u78, and you just moved from Florida (32169) to Phoenix (85033). Unfortunately your address is still the old one, and you want to update it. Your current address should be in your order, and you do not want to reveal it. Also, you want to know what is the price of the cheapest available t-shirt right now, and if you can order it through the agent.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u78",
                    "zip": "85033",
                },
            ),
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u78",
                    "zip": "32169",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "u78"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5285031"},
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "u78",
                    "address1": "157 Oak Street",
                    "address2": "Suite 258",
                    "city": "Phoenix",
                    "state": "AZ",
                    "country": "USA",
                    "zip": "85033",
                },
            ),
            Action(
                name="list_all_product_types",
                kwargs={},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9523456873"},
            ),
        ],
        outputs=['46.66'],
    ),
    Task(
        annotator="0",
        user_id="k44",
        instruction="You are User k44, and your email address is user.k44@example.com. You want to know how much balance your gift card has. Also, for your recent order, you want to know whether you used your visa, mastercard, or amex credit card. You also wonder if you can apply the gift card balance to the order. If not, you want to change your payment method to visa, because the other two cards have a lot of balance.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.k44@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "k44"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4923227"},
            ),
            Action(
                name="modify_pending_order_payment",
                kwargs={"order_id": "#W4923227", "payment_method_id": "credit_card_8897086"},
            ),
        ],
        outputs=['60', 'mastercard'],
    ),
    Task(
        annotator="0",
        user_id="p39",
        instruction="Your name is User p39, and you live in 445 Maple Drive, Suite 394, Fort Worth, Texas, 76165. You ordered some items, but you have two problems. First, the 1000-piece intermediate jigsaw puzzle might be too hard for your little kid; you wonder if you can change it to the easiest one with fewest pieces. Second, you might have typed your address wrong. You want to verify this, and potentially correct all order addresses and your user address. Make sure you mention these two problems at the same time in the same order.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "p39",
                    "zip": "76165",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "p39"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9583042"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4082615"},
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W9583042",
                    "address1": "445 Maple Drive",
                    "address2": "Suite 394",
                    "city": "Fort Worth",
                    "state": "TX",
                    "country": "USA",
                    "zip": "76165",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W4082615",
                    "address1": "445 Maple Drive",
                    "address2": "Suite 394",
                    "city": "Fort Worth",
                    "state": "TX",
                    "country": "USA",
                    "zip": "76165",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "p39",
                    "address1": "445 Maple Drive",
                    "address2": "Suite 394",
                    "city": "Fort Worth",
                    "state": "TX",
                    "country": "USA",
                    "zip": "76165",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1808611083"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4082615"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4082615",
                    "item_ids": ["9779102705"],
                    "new_item_ids": ["1096508426"],
                    "payment_method_id": "paypal_4768213",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="p39",
        instruction="Your name is User p39, and you live in 445 Maple Drive, Suite 394, Fort Worth, Texas, 76165. You ordered some items, but realized you might have typed your address wrong. You want to verify this, and potentially correct all order addresses and your user address. After this, you would like to check the jigsaw puzzle you ordered, and if it's not shipped yet, you want to change it to the easiest jigsaw puzzle (easiest level, least pieces) because your kid is too young. By default you use PayPal.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "p39",
                    "zip": "76165",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "p39"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9583042"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4082615"},
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W9583042",
                    "address1": "445 Maple Drive",
                    "address2": "Suite 394",
                    "city": "Fort Worth",
                    "state": "TX",
                    "country": "USA",
                    "zip": "76165",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W4082615",
                    "address1": "445 Maple Drive",
                    "address2": "Suite 394",
                    "city": "Fort Worth",
                    "state": "TX",
                    "country": "USA",
                    "zip": "76165",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "p39",
                    "address1": "445 Maple Drive",
                    "address2": "Suite 394",
                    "city": "Fort Worth",
                    "state": "TX",
                    "country": "USA",
                    "zip": "76165",
                },
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1808611083"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4082615"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4082615",
                    "item_ids": ["9779102705"],
                    "new_item_ids": ["1096508426"],
                    "payment_method_id": "paypal_4768213",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="h30",
        instruction="You are User h30, you live in Denver CO 80239, and your daughter lives in Chicago. You order some things for her but she has not received them, so you want to know which address the order was sent to, the tracking number, and if the order is still in transit. You also want to check the storage of the tablet you ordered. Lastly, you want to change your default address to your daughter's address so that you don't have to change it every time you order something for her.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "h30",
                    "zip": "80239",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "h30"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W1588712"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7895761"},
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "h30",
                    "address1": "943 Maple Drive",
                    "address2": "Suite 356",
                    "city": "Chicago",
                    "state": "IL",
                    "country": "USA",
                    "zip": "60621",
                },
            ),
        ],
        outputs=['840887978435', '943 Maple Drive', 'Suite 356', 'Chicago', 'IL', '60621', '64GB'],
    ),
    Task(
        annotator="0",
        user_id="p59",
        instruction="You are User p59, residing in Philadelphia 19031. You want to change the Desk Lamp in order #W9300146 that you've placed for the cheapest Desk Lamp that's available. Any price difference should go to a gift card. You also want to know how much you get back in total.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "p59",
                    "zip": "19031",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9300146"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "6817146515"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "135.24 - 153.23"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9300146",
                    "item_ids": ["9190635437"],
                    "new_item_ids": ["5320792178"],
                    "payment_method_id": "gift_card_7245904",
                },
            ),
        ],
        outputs=['17.99'],
    ),
    Task(
        annotator="0",
        user_id="u22",
        instruction="You are User u22 living in Denver, USA, 80273. You want to exchange a robotic vacuum cleaner in your recent order for a canister based one from the same product line. When asked for order ID, provide 9502127 first. If that doesn't work, respond exactly with 'I forgot the W at the beginning'. *If and only if* the agent gives you several options for the new vacuum, go for the bagless version (don't mention this if the agent just provides you one option). Ask the agent about receiving a gift card for the price difference instead of the original payment method, if possible.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u22",
                    "zip": "80273",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9502127"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "1762337868"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "652.61 - 642.72"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W9502127",
                    "item_ids": ["6259501109"],
                    "new_item_ids": ["7958300294"],
                    "payment_method_id": "paypal_2433177",
                },
            ),
        ],
        outputs=['9.89'],
    ),
    Task(
        annotator="0",
        user_id="u22",
        instruction="You are User u22 living in Denver, USA, 80273. You want to return an air purifier and a vacuum cleaner in your recent order. When asked for order ID, provide 9502126 first. If the agent asks you to double check, then say that you made a mistake and provide 9502127. If that doesn't work, say that you forgot the 'W' at the beginning. If the agent asks you for which vacuum cleaner, mention the robotic one. Ask the agent explicitly to provide the refund within 3 days and the total amount of refund you should expect. After the return is complete, ask the agent about the total amount you paid for the remaining items in the same order.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u22",
                    "zip": "80273",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#9502126"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#9502127"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9502127"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "652.61 + 473.43"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9502127",
                    "item_ids": ["6259501109", "9534205511"],
                    "payment_method_id": "paypal_2433177",
                },
            ),
            Action(
                name="calculate",
                kwargs={"expression": "2623.69 - 1126.04"},
            ),
        ],
        outputs=['1126.04', '1497.65'],
    ),
    Task(
        annotator="0",
        user_id="u22",
        instruction="You are User u22 living in Denver, USA, 80273. You want to return an air purifier and a vacuum cleaner in your recent order. When asked for order ID, provide 9502126 first. If the agent asks you to double check, then say that you made a mistake and provide 9502127. If that doesn't work, say that you forgot the 'W' at the beginning. If the agent asks you for which vacuum cleaner, mention the canister one. Ask the agent explicitly to provide the refund within 3 days and the total amount of refund you should expect. After the return is complete, ask the agent about the total amount you paid for the remaining items in the same order.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u22",
                    "zip": "80273",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#9502126"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#9502127"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9502127"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "622.12 + 473.43"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9502127",
                    "item_ids": ["2872451762", "9534205511"],
                    "payment_method_id": "paypal_2433177",
                },
            ),
            Action(
                name="calculate",
                kwargs={"expression": "2623.69 - 1095.55"},
            ),
        ],
        outputs=['1095.55', '1528.14'],
    ),
    Task(
        annotator="0",
        user_id="u22",
        instruction="You are User u22 living in Denver, USA, 80273. You want to return an air purifier that you received since it doesn't work well. You want the refund on your original method of payment. Also, check at the end whether you are able to return the vacuum cleaner. Since you are not sure yet, don't process anything.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "u22",
                    "zip": "80273",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "u22"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W1436802"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5282037"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9502127"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9502127",
                    "item_ids": ["9534205511"],
                    "payment_method_id": "paypal_2433177",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="p59",
        instruction="You are User p59, residing in Philadelphia 19031. You mistakenly ordered a Wireless Earbud with an IPX7 water resistance level, but you don't require this feature. You wish to exchange it for one with the same water resistance level as the other Wireless Earbuds that you've purchased. In fact, you want to exchange it to the cheapest earbud item from the rest of that order.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "p59",
                    "zip": "19031",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "p59"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4316152"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9311069"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W9300146"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3220203"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3470184"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9924732112"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "258.97 - 232.49"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3470184",
                    "item_ids": ["2757705742"],
                    "new_item_ids": ["1646531091"],
                    "payment_method_id": "gift_card_7245904",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="q39",
        instruction="You're User q39, living in Jacksonville 32278. You're in a rush and you want to undo cancelling an order that you've previously placed. Be insistent that the customer service agent should undo the cancellation and ensure that the order is delivered as soon as possible. Do NOT mention the actual items that were in the order, just that you want to undo the cancellation and receive all the items that were in the initial order as soon as possible.",
        actions=[
            Action(
                name="transfer_to_human_agents",
                kwargs={
                    "summary": "The user urgently needs to undo a cancellation of an order and insists on receiving the items from the initial order as soon as possible. The user acknowledges the policy but requests exceptional measures due to the urgency of the situation.",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b38",
        instruction="You are User b38, residing in San Antonio, 78260. You want to return the digital camera that you received. You guess that the order number is #W8855135, but you're not 100 percent sure. Insist that you want to return the camera and get a refund to the original payment method.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b38",
                    "zip": "78260",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W8855135"},
            ),
            Action(
                name="list_all_product_types",
                kwargs={},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8940227892"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b38"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4689314"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W4689314",
                    "item_ids": ["5996159312"],
                    "payment_method_id": "credit_card_8105988",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b38",
        instruction="You are User b38, residing in San Antonio, 78260. The digital camera you received doesn't zoom as far as you expected. You use the camera for bird-watching and want to exchange it for a camera that has the maximum zoom capacity. Price is not an issue, but ensure all the other specifications of the camera are the same, except for the zoom capacity which has to be maximized. You want the exchange to be completed as soon as possible. You want to use your PayPal account for any additional payment.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b38",
                    "zip": "78260",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b38"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4689314"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "8940227892"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4689314",
                    "item_ids": ["5996159312"],
                    "new_item_ids": ["9228757377"],
                    "payment_method_id": "paypal_8194385",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b38",
        instruction="You are User b38, residing in San Antonio, 78260. The bicycle you received was damaged during delivery, and you want to get a refund. The bike was very expensive and you would like to receive the refund as soon as possible. You want the refund to be credited to your original credit card.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "b38",
                    "zip": "78260",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "b38"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4689314"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W8855135"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3916020"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W3916020",
                    "item_ids": ["7758198585"],
                    "payment_method_id": "credit_card_8105988",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="y21",
        instruction="You are User y21, and your email is user.y21@example.com. You live in Philadelphia, and you are a loyal customer. But you just faced a financial issue and want to cancel or return all possible orders except the boots. You are happy to exchange it for boots of the exact same size and material to get maximum money back, but only if they are cheaper than what you have paid. You wonder how much money you can get back today.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.y21@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "y21"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2586676"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5400801"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4597054"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4836353"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7773202"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7342738"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W4836353", "reason": "no longer needed"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W7342738", "reason": "no longer needed"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W4597054",
                    "item_ids": [
                        "5669664287",
                        "4900990404",
                        "9862136885",
                        "6777246137",
                    ],
                    "payment_method_id": "gift_card_3491931",
                },
            ),
        ],
        outputs=['3646.68'],
    ),
    Task(
        annotator="0",
        user_id="y21",
        instruction="You are User y21, and your email is user.y21@example.com. You live in Philadelphia, and you are a loyal customer. But you just faced a financial issue and want to cancel or return all possible orders.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "user.y21@example.com"},
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "y21"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2586676"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5400801"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4597054"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4836353"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7773202"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7342738"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W4836353", "reason": "no longer needed"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W7342738", "reason": "no longer needed"},
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W4597054",
                    "item_ids": [
                        "5669664287",
                        "4900990404",
                        "9862136885",
                        "6777246137",
                    ],
                    "payment_method_id": "gift_card_3491931",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7773202",
                    "item_ids": ["8277474082"],
                    "payment_method_id": "gift_card_3491931",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="d53",
        instruction="You are User d53 living in San Diego, 92133. You wonder when your air purifier is arriving. If it has not been shipped yet, you want to cancel the air purifier from your order. If you cannot cancel just the air purifier, you want to modify it to the cheapest possible air purifier, and refund to the gift card. You do not remember your gift card id but it should be in your user account. If you cannot modify it or refund to the gift card, you don't do anything.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "d53",
                    "zip": "92133",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "d53"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5838674"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4284542"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2782744"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "3821016478"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4284542",
                    "item_ids": ["8302289002"],
                    "new_item_ids": ["9534205511"],
                    "payment_method_id": "gift_card_9368765",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="d53",
        instruction="You are User d53 living in San Diego, 92133. You wonder when your order W4284542 is arriving. If it has not been shipped yet, you want to cancel the air purifier from your order. If you cannot cancel just the air purifier, you want to cancel the whole order and refund to gift card. If you cannot refund it to a gift card, you do not cancel anything.",
        actions=[
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="d53",
        instruction="You are User d53 living in San Diego, 92133. You want to modify two items in an order you just received: a coffee machine and a laptop. For the coffee machine, you want to keep the capacity and type the same, but change the pressure lower to 8 bar. If 8 bar is not possible, you want 9 bar. If 9 bar is not possible, you want 7 bar. If 7, 8, and 9 are not possible, you do not exchange the coffee machine. For the laptop, you want to exchange to the cheapest i7 or above, and you do not care about other specs. If a price difference is necessary, you prefer gift card payment. If that is not possible, you would use credit card.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "d53",
                    "zip": "92133",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "d53"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5838674"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4354588079"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4760268021"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W5838674",
                    "item_ids": ["7441167885", "3478699712"],
                    "new_item_ids": ["3815173328", "6017636844"],
                    "payment_method_id": "gift_card_9368765",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w43",
        instruction=(
            "You are User w43 from San Jose, CA, 95154. You recently placed two orders, "
            "and now you would like to make several changes and checks. You'll first inquire "
            "about the status difference between your two orders, #W2702727 and #W8268610, "
            "since both are \"pending,\" but one was placed much earlier in the year. You are "
            "considering cancelling the older order as you find the wait time unreasonable. "
            "If the agent cannot guarantee the older order will be processed within 5 days, "
            "you want to cancel it. You also want to confirm the total price of the refund.\n\n"
            "For order #W2702727, you intend to switch the shipping address to your new home "
            "in a different city because you plan to move prior to its delivery next month. "
            "Your new address is 1234 Elm St, Springfield, IL, 62701. You want the agent to "
            "confirm the change and ensure the order will be delivered to the new address. "
            "You also want to confirm the total price of the order after the address change.\n\n"
        ),
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "w43",
                    "zip": "95154",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={
                    "order_id": "#W2702727",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={
                    "order_id": "#W8268610",
                },
            ),
            Action(
                name="calculate",
                kwargs={
                    "expression": "164.28",
                },
            ),
            Action(
                name="cancel_pending_order",
                kwargs={
                    "order_id": "#W8268610",
                    "reason": "no longer needed",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W2702727",
                    "address1": "1234 Elm St",
                    "address2": "",
                    "city": "Springfield",
                    "state": "IL",
                    "country": "USA",
                    "zip": "62701",
                },
            ),
        ],
        outputs=[
            "164.28",
            "625.60",
        ],
    ),
    Task(
        annotator="0",
        user_id="h49",
        instruction="You are User h49 from Houston TX, 77004. You want to change your wireless earbuds in order W5061109 to blue colored ones. Provide all details upfront in your very first message and ask the agent to resolve as soon as possible. You want the price to be the same or lower, which you want the agent to verify explicitly. If and only if the agent provides several options, you want the option without water resistance.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "h49",
                    "zip": "77004",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5061109"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9924732112"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5061109",
                    "item_ids": ["3694871183"],
                    "new_item_ids": ["6077640618"],
                    "payment_method_id": "paypal_3742148",
                },
            ),
        ],
        outputs=['242.92'],
    ),
    Task(
        annotator="0",
        user_id="h49",
        instruction="You are User h49 from Houston TX, 77004. You want to change your wireless earbuds in order W5061109 to blue colored ones. Provide all details upfront and ask the agent to resolve as soon as possible. You want the price to be the same or lower.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "h49",
                    "zip": "77004",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5061109"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9924732112"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "256.67 - 226.49"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5061109",
                    "item_ids": ["3694871183"],
                    "new_item_ids": ["8555936349"],
                    "payment_method_id": "paypal_3742148",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="h49",
        instruction="You are User h49 from Houston TX, 77004. You want to check and modify a recent order you placed. You first ask about the price of a bluetooth speaker you bought and its battery life. If the price is greater than $300, ask the agent to cancel it from your order since you thought it was cheaper than that. Ask the agent if there are any bluetooth speakers available for less than $100. If there are, ask the agent to add the cheapest one to your order. Finally, ask the agent to confirm the total price of your new order. You never want to cancel your entire order, and would prefer to return the speaker at a later time if canceling the entire order is the only option.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "h49",
                    "zip": "77004",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "h49"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5797164"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5061109"},
            ),
            Action(
                name="list_all_product_types",
                kwargs={},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4768869376"},
            ),
        ],
        outputs=['302.67', '20 hours'],
    ),
    Task(
        annotator="0",
        user_id="h49",
        instruction="You are User h49 from Houston TX, 77004. You want to check and modify a recent order you placed. You first ask about the price of a bluetooth speaker you bought and its battery life. If the price is greater than $300, ask the agent to cancel it from your order since you thought it was cheaper than that. Ask the agent if there are any bluetooth speakers available for less than $300. If there are, ask the agent to add the cheapest one to your order. Finally, ask the agent to confirm the total price of your new order. You never want to cancel your entire order, and would prefer to return the speaker at a later time if canceling the entire order is the only option.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "h49",
                    "zip": "77004",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "h49"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5797164"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5061109"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "4768869376"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "1319.43 - 302.67 + 271.89"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5061109",
                    "item_ids": ["3254583681"],
                    "new_item_ids": ["2635605237"],
                    "payment_method_id": "paypal_3742148",
                },
            ),
        ],
        outputs=['302.67', '20 hours', '1288.65'],
    ),
    Task(
        annotator="0",
        user_id="m92",
        instruction="You are User m92. You live in Chicago 60623. You want to exchange the camera for the highest resolution, waterproof camera that you can get with the previous purchased price.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "m92",
                    "zip": "60623",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "m92"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W7464385"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W8499625"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W1279004"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "3377618313"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W7464385",
                    "item_ids": ["1810466394"],
                    "new_item_ids": ["6700049080"],
                    "payment_method_id": "paypal_1261484",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W7464385",
                    "item_ids": ["1810466394"],
                    "new_item_ids": ["6700049080"],
                    "payment_method_id": "paypal_1261484",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="z86",
        instruction="You are User z86 from San Jose CA, 95190. You want to exchange the bookshelf from your most recent order for a camera that is closest in price but not more expensive than the bookshelf.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "z86",
                    "zip": "95190",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "z86"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5362037"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="g47",
        instruction="You are User g47. You want to change the luggage set in your order for a coat. You live in Phoenix, AZ 85025. Your goal is to change the order. If there is no way to do that, return the item specifically. If there are any issues, cancel the entire order.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "g47",
                    "zip": "85025",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "g47"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3361211"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W3586556"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W3361211", "reason": "no longer needed"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="j71",
        instruction="You are User j71 living in Seattle WA 98187. If asked for your zip code, say that it is 98178 first (common mistake), then correct yourself and say 98186 if an error is found. If that fails, then say 98187. You want to check how much you paid for the order that you most recently placed. You are not sure how long ago the order was placed.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "j71",
                    "zip": "98178",
                },
            ),
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "j71",
                    "zip": "98186",
                },
            ),
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "j71",
                    "zip": "98187",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "j71"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6729841"},
            ),
        ],
        outputs=['829.43'],
    ),
    Task(
        annotator="0",
        user_id="j71",
        instruction="You are User j71 living in Seattle WA 98187. If asked for your zip code, say that it is 98178 first (common mistake), then correct yourself and say 98187 if an error is found. You want to check how much you paid for the order that you most recently placed. You are not sure how long ago the order was placed.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "j71",
                    "zip": "98178",
                },
            ),
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "j71",
                    "zip": "98187",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "j71"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6729841"},
            ),
        ],
        outputs=['829.43'],
    ),
    Task(
        annotator="0",
        user_id="s12",
        instruction="You are User s12 living in New York, New York, 10192. You want to return an item you just received: a laptop. You think that you ordered it around April 2023 but are not sure. You want to return it because you found a better deal elsewhere. You want to return it for a full refund. If it cannot be returned, see if it can be canceled.",
        actions=[
            Action(
                name="find_user_id_by_name_zip",
                kwargs={
                    "first_name": "User",
                    "last_name": "s12",
                    "zip": "10192",
                },
            ),
            Action(
                name="get_user_details",
                kwargs={"user_id": "s12"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W2417020"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W2417020", "reason": "no longer needed"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="s61",
        instruction="Your name is User s61 and your zip code is 98193. You recently received a helmet but you are not happy with it and want to exchange it. The size is too small and you want medium, plus you want high ventilation. If multiple colors are available, you prefer blue. You prefer to use the original payment to pay for the price difference, and you want to know how much you need to pay today.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3947049",
                    "item_ids": ["3358616356"],
                    "new_item_ids": ["9013366374"],
                    "payment_method_id": "credit_card_7901829",
                },
            ),
        ],
        outputs=['22.55'],
    ),
    Task(
        annotator="0",
        user_id="m93",
        instruction="Your name is User m93 and your zip code is 28243. You made a mistake and placed an order sent to your son's address in Washington DC, and you want to modify it to your default address in Charlotte (you do not want to mention it, but it is in your user profile so the agent can look it up). You also want to adjust the desk lamp to be black color, and the backpack to be medium size and polyester material instead. If multiple colors are available for the backpack, you prefer grey. If the agent asks for a payment method, you say gift card initially. If the agent does not allow it or asks you to confirm it, you change your mind to PayPal and decide to only modify the backpack.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W5270061",
                    "address1": "159 Hickory Lane",
                    "address2": "Suite 995",
                    "city": "Charlotte",
                    "country": "USA",
                    "state": "NC",
                    "zip": "28243",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5270061",
                    "item_ids": ["2492465580"],
                    "new_item_ids": ["5917587651"],
                    "payment_method_id": "paypal_7729105",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m93",
        instruction="Your name is User m93 and your zip code is 28243. You made a mistake and placed an order sent to your son's address in Washington DC. You want to modify it to your default address in Charlotte (you do not want to mention it, but it is in your user profile so the agent can look it up). You also want to adjust the desk lamp to be black color, and the backpack to be medium size and polyester material instead. If multiple colors are available for the backpack, you prefer grey. If the agent asks for a payment method, you say gift card initially. If the agent does not allow it or asks you to confirm it, you change your mind to PayPal, and decide to only modify the backpack. Make sure you briefly mention the two things at the same time at the beginning, but first mention the modification then the address.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W5270061",
                    "address1": "159 Hickory Lane",
                    "address2": "Suite 995",
                    "city": "Charlotte",
                    "country": "USA",
                    "state": "NC",
                    "zip": "28243",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5270061",
                    "item_ids": ["2492465580"],
                    "new_item_ids": ["5917587651"],
                    "payment_method_id": "paypal_7729105",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b76",
        instruction="Your name is User b76 and your email is user.b76@example.com. You want to return everything you just bought except the coffee machine.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W5272531",
                    "item_ids": [
                        "7228247242",
                        "2698416822",
                        "8098621301",
                        "3320557165",
                    ],
                    "payment_method_id": "credit_card_6824399",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="n20",
        instruction="Your name is User n20 and your zip code is 85033. You recently bought a laptop, but you want to exchange it to i9 CPU. If multiple storage options are available, you prefer 256GB SSD. If multiple colors are available, you prefer silver. You also have a pending order with five items (you don't remember the order ID), and you want to cancel it because you no longer need these items.",
        actions=[
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W3189752", "reason": "no longer needed"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5166363",
                    "item_ids": ["3334537816"],
                    "new_item_ids": ["3265035808"],
                    "payment_method_id": "credit_card_4466831",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="c76",
        instruction="Your name is User c76 and your email is user.c76@example.com. For #W6908222, exchange Wireless Earbuds {'color': 'blue', 'battery life': '8 hours', 'water resistance': 'IPX4'} for {'color': 'black', 'battery life': '4 hours', 'water resistance': 'not resistant'}.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W6908222",
                    "item_ids": ["8555936349"],
                    "new_item_ids": ["4063058357"],
                    "payment_method_id": "paypal_4518393",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="a42",
        instruction="Your name is User a42 and your zip code is 94128. You ordered a fleece jacket by mistake and want to remove it from your pending order. If removing one item is not possible, cancel the whole order. You also want to modify the skateboard to maple material, 34 inch, graphic. If not availabe, cancel the order so that you can order again. You also want to know the total prices for the grills you have paid for.",
        actions=[
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W8367380", "reason": "ordered by mistake"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W1242543", "reason": "no longer needed"},
            ),
        ],
        outputs=['1939.05'],
    ),
    Task(
        annotator="0",
        user_id="h37",
        instruction="Your name is User h37 and your zip code is 94183. You ordered a perfume and you just tried a little bit and you really like it. You want to get the maximum size available for it. If the agent cannot help with placing a new order, exchange your current one to the largest size available.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W1671835",
                    "item_ids": ["5081446110"],
                    "new_item_ids": ["3399869890"],
                    "payment_method_id": "paypal_6918118",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="j70",
        instruction="Your name is User j70 and your email is user.j70@example.com. For #W5056519, change the address to the same one as #W8277957. For #W5056519, exchange Makeup Kit {'skin tone': 'light', 'kit size': 'professional', 'brand': 'Brand B'} for {'skin tone': 'dark', 'brand': 'Brand A'}; Cancel order #W5995614 because you ordered things by mistake.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W5056519",
                    "address1": "380 Maple Drive",
                    "address2": "Suite 960",
                    "city": "San Diego",
                    "country": "USA",
                    "state": "CA",
                    "zip": "92101",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W5056519",
                    "item_ids": ["7902309762"],
                    "new_item_ids": ["1573035764"],
                    "payment_method_id": "credit_card_3095586",
                },
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W5995614", "reason": "ordered by mistake"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="e70",
        instruction="Your name is User e70 and your zip code is 32190. You just bought a water bottle with 500ml but you regret it, and you want to change it to the other bottle you just placed with 1000ml capacity. If the exact item is not available any more, you can allow the material to be different.",
        actions=[
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W8661412",
                    "item_ids": ["3453331371"],
                    "new_item_ids": ["2439754078"],
                    "payment_method_id": "credit_card_7239357",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b39",
        instruction="Your name is User b39 and your email is user.b39@example.com. For #W7209932, exchange T-Shirt {'color': 'blue', 'size': 'S', 'material': 'polyester', 'style': 'v-neck'} for {'color': 'red', 'size': 'XXL', 'material': 'cotton', 'style': 'crew neck'}. Use the gift card.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W7209932",
                    "item_ids": ["5047954489"],
                    "new_item_ids": ["9354168549"],
                    "payment_method_id": "gift_card_2611937",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="t10",
        instruction="Your name is User t10 and your email is user.t10@example.com. Due to some life changes, you no longer need hiking boots, watch, keyboard, charger, jacket, and running shoes. If cancelling part of the order is not possible, you want to cancel the whole order.",
        actions=[
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W3289292", "reason": "no longer needed"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W9722559", "reason": "no longer needed"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="d60",
        instruction="Your name is User d60 and your zip code is 46281. You received two tablets and you only need one. You want to return the more expensive one and refund to credit card. If refund to credit card is not possible, you want to return everything on that order and refund to gift card.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9571698",
                    "item_ids": [
                        "5952720925",
                        "9973034634",
                        "7381052709",
                        "6065192424",
                    ],
                    "payment_method_id": "gift_card_7250692",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="d60",
        instruction="Your name is User d60 and your zip code is 46281. You received two tablets and you only need one. You want to return the more expensive one and refund to credit card. If refund to credit card is not possible, you refund to gift card.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9571698",
                    "item_ids": ["6065192424"],
                    "payment_method_id": "gift_card_7250692",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="d60",
        instruction="Your name is User d60 and your zip code is 46281. You received two tablets and you only need one. You want to return the less expensive one and refund to credit card. But if the agent asks for confirmation, you change your mind and return the more expensive one and refund to gift card.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9571698",
                    "item_ids": ["6065192424"],
                    "payment_method_id": "gift_card_7250692",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="s41",
        instruction="Your name is User s41 and your email is user.s41@example.com. You want to exchange your Fleece Jacket for a large red Fleece Jacket with a half zipper",
        actions=[
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W2466703",
                    "item_ids": ["9385662952"],
                    "new_item_ids": ["8733974883"],
                    "payment_method_id": "paypal_7529813",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="s41",
        instruction="Your name is User s41 and your email is user.s41@example.com. You want to exchange your Fleece Jacket to a red color and half zipper one. You also want to want to change your default address to your Washington DC address (which you do not want to reveal but is in one of the orders).",
        actions=[
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W2466703",
                    "item_ids": ["9385662952"],
                    "new_item_ids": ["8733974883"],
                    "payment_method_id": "paypal_7529813",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "s41",
                    "address1": "565 Maple Drive",
                    "address2": "Suite 501",
                    "city": "Washington",
                    "country": "USA",
                    "state": "DC",
                    "zip": "20307",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="s41",
        instruction="Your name is User s41 and your email is user.s41@example.com. You want to modify all your pending order addresses to the Washington DC address (which you do not want to reveal but is in one of the orders), along with your user default address.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W2166301",
                    "address1": "565 Maple Drive",
                    "address2": "Suite 501",
                    "city": "Washington",
                    "country": "USA",
                    "state": "DC",
                    "zip": "20307",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W2466703",
                    "address1": "565 Maple Drive",
                    "address2": "Suite 501",
                    "city": "Washington",
                    "country": "USA",
                    "state": "DC",
                    "zip": "20307",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W6832752",
                    "address1": "565 Maple Drive",
                    "address2": "Suite 501",
                    "city": "Washington",
                    "country": "USA",
                    "state": "DC",
                    "zip": "20307",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "s41",
                    "address1": "565 Maple Drive",
                    "address2": "Suite 501",
                    "city": "Washington",
                    "country": "USA",
                    "state": "DC",
                    "zip": "20307",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m31",
        instruction="Your name is User m31 and your email is user.m31@example.com. You want to change the book shelf to a 4 foot one, but with the same material and color. If it is not available, cancel the whole order and you will buy again. If the agent asks for the cancellation reason, you say you ordered by mistake.",
        actions=[
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W8835847", "reason": "ordered by mistake"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="u91",
        instruction="Your name is User u91 and your zip code is 98157. You want to know what is the cheapest availabe mechanical keyboard right now and its options. If it is less than $200 you want to exchange your current one to it. If not, return your current one.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W4680753",
                    "item_ids": ["9690244451"],
                    "payment_method_id": "paypal_2417743",
                },
            ),
        ],
        outputs=['226.11', 'tactile', 'white', 'full'],
    ),
    Task(
        annotator="0",
        user_id="e70",
        instruction="Your name is User e70 and your email is user.e70@example.com. You want to know if the digital camera you just bought is 10x zoom. If not, modify the item to 10x zoom without changing the other options. If 10x zoom is not available, cancel the order with the reason of no longer needed. If it is available but the price is more than $3000, cancel the order with the reason of ordered by mistake.",
        actions=[
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W9284598", "reason": "ordered by mistake"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w68",
        instruction="Your name is User w68 and your zip code is 78705. You are upset about the quality of the two skateboards you just bought. You want to return them and refund to credit card. If the agent asks for confirmation, do not say yes, because you also want to return the smart watch. You also want to return the e-reader you just bought. If the same item is availabe online, you're willing to exchange it to the same item. If not, you want to return it and refund to credit card.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7553978",
                    "item_ids": ["4545791457", "3098764622", "1631806422"],
                    "payment_method_id": "credit_card_5902940",
                },
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3239882",
                    "item_ids": ["9494281769"],
                    "new_item_ids": ["9494281769"],
                    "payment_method_id": "credit_card_5902940",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="w68",
        instruction="Your name is User w68 and your zip code is 78705. You are angry about the quality of the two skateboards you just bought. You want to return them and refund to credit card. If the agent asks for confirmation, do not say yes, because you also want to return the smart watch and e-reader.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W7553978",
                    "item_ids": ["4545791457", "3098764622", "1631806422"],
                    "payment_method_id": "credit_card_5902940",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W3239882",
                    "item_ids": ["9494281769"],
                    "payment_method_id": "credit_card_5902940",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="g12",
        instruction="Your name is User g12 and your zip code is 32255. You received a laptop and you want to exchange it to i7 processor, 8GB, 1TB SSD. If the agent asks for which laptop, it is 15-inch, 32GB.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4073673",
                    "item_ids": ["2216662955"],
                    "new_item_ids": ["9844888101"],
                    "payment_method_id": "credit_card_3677959",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="g12",
        instruction="Your name is User g12 and your zip code is 32255. You received a laptop and you want to exchange it to i7 processor, 8GB, 1TB SSD. If the agent asks for which laptop, it is 15-inch, 16GB.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W2905754",
                    "item_ids": ["3478699712"],
                    "new_item_ids": ["9844888101"],
                    "payment_method_id": "credit_card_3677959",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="g12",
        instruction="Your name is User g12 and your zip code is 32255. You received a laptop and you want to exchange it to i7 processor, 8GB, 1TB SSD. If the agent asks for which laptop, it is 15-inch, 32GB.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4073673",
                    "item_ids": ["2216662955"],
                    "new_item_ids": ["9844888101"],
                    "payment_method_id": "credit_card_3677959",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="g12",
        instruction="Your name is User g12 and your zip code is 32255. You received a laptop and you want to exchange it to i7 processor, 8GB, 1TB SSD. If the agent asks for which laptop, it is 15-inch, and it is actually two laptops that you want to exchange. You want to know how much you need to pay today in total.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W2905754",
                    "item_ids": ["3478699712"],
                    "new_item_ids": ["9844888101"],
                    "payment_method_id": "credit_card_3677959",
                },
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4073673",
                    "item_ids": ["2216662955"],
                    "new_item_ids": ["9844888101"],
                    "payment_method_id": "credit_card_3677959",
                },
            ),
        ],
        outputs=['167.87', '60.78', '107.09'],
    ),
    Task(
        annotator="0",
        user_id="f97",
        instruction="Your name is User f97 and your zip code is 91148. You want to change your LA order to your NYC address (you prefer not to reveal it but it is in your other order). You also want to exchange the Bluetooth Speaker to be the cheapest green type.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W6750959",
                    "address1": "476 Maple Drive",
                    "address2": "Suite 432",
                    "city": "New York",
                    "country": "USA",
                    "state": "NY",
                    "zip": "10093",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W6750959",
                    "item_ids": ["3254583681"],
                    "new_item_ids": ["9440686670"],
                    "payment_method_id": "paypal_8080730",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="f97",
        instruction="Your name is User f97 and your zip code is 91148. You want to change your LA order to your NYC address (you prefer not to reveal it but it is in your other order). You also want to exchange the Bluetooth Speaker to be the cheapest green type. Make sure you mention the two requests at the same time to the agent, but mention the exchange first.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W6750959",
                    "address1": "476 Maple Drive",
                    "address2": "Suite 432",
                    "city": "New York",
                    "country": "USA",
                    "state": "NY",
                    "zip": "10093",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W6750959",
                    "item_ids": ["3254583681"],
                    "new_item_ids": ["9440686670"],
                    "payment_method_id": "paypal_8080730",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b38",
        instruction="Your name is User b38 and your zip code is 78260. You want to exchange your bicycle to a larger frame size for your kid. The jigsaw puzzle in the same order also needs to be exchanged. You want the same difficulty, but a 1000 more pieces, and you prefer the animal theme more than the art theme if both are available. Make sure you mention these at the same time. You also want to exchange your camera to slightly lower resolution, without changing the other options. If the agent asks for confirmation, mention that you would prefer the other card as payment or refund method. Lastly, you want to cancel the skateboard order. If you cannot cancel one single item, you are okay with cancelling the whole order, with the reason of no longer needed.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4689314",
                    "item_ids": ["5996159312"],
                    "new_item_ids": ["8363011723"],
                    "payment_method_id": "credit_card_3951670",
                },
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3916020",
                    "item_ids": ["7758198585", "4068787148"],
                    "new_item_ids": ["5606522780", "6245746168"],
                    "payment_method_id": "credit_card_8105988",
                },
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W8855135", "reason": "no longer needed"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="b38",
        instruction="Your name is User b38 and your zip code is 78260. You want to exchange your bicycle to a larger frame size for your kid. The higsaw puzzle in the same order also needs to be exchanged. You want the same difficulty, but a 1000 more pieces, and you prefer the art theme more than animal theme if both are available. Make sure you mention these at the same time. You also want to exchange your camera to a slightly lower resolution, without changing the other options. For both orders, you would prefer the visa card as payment or refund method. Lastly, you want to cancel the skateboard order. If you cannot cancel one single item, you are okay with cancelling the whole order. You will do this yourself on the website and there is no need for the agent to help.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4689314",
                    "item_ids": ["5996159312"],
                    "new_item_ids": ["8363011723"],
                    "payment_method_id": "credit_card_3951670",
                },
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3916020",
                    "item_ids": ["7758198585", "4068787148"],
                    "new_item_ids": ["5606522780", "5546244844"],
                    "payment_method_id": "credit_card_3951670",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="s72",
        instruction="Your name is User s72 and your zip code is 85049. You want to return your luggage set and get the exact same item in red, and return your skateboard in the same order for one with {'length': '34 inch', 'design': 'custom'}; You also want to return the hiking boots.",
        actions=[
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W3295833",
                    "item_ids": ["8926329222", "5312063289"],
                    "new_item_ids": ["7160999700", "6956751343"],
                    "payment_method_id": "credit_card_3261838",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W8488728",
                    "item_ids": ["5676696062"],
                    "payment_method_id": "paypal_3650980",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="j71",
        instruction="Your name is User j71 and your zip code is 98187. You just placed an order with two watches. You want to change its address to your New York address (you don't want to reveal it but it's in your other order). You also want to modify the silicone watch to a metal one. If multiple colors available, you prefer white. For the air purifier you received along with a speaker, you want to exchange the purifier to large size and night mode, but still with HEPA filter.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W4219264",
                    "address1": "144 Lakeview Drive",
                    "address2": "Suite 925",
                    "city": "New York",
                    "country": "USA",
                    "state": "NY",
                    "zip": "10228",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4219264",
                    "item_ids": ["8886009523"],
                    "new_item_ids": ["2407258246"],
                    "payment_method_id": "credit_card_1620755",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W6729841",
                    "item_ids": ["3076708684"],
                    "new_item_ids": ["8302289002"],
                    "payment_method_id": "credit_card_1620755",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="j71",
        instruction="Your name is User j71 and your zip code is 98187. You just placed an order with two watches. You want to change its address to your New York address (you don't want to reveal it but it's in your other order). You also want to modify the silicone watch to a metal one. If multiple colors available, you prefer white. For the air purifier you received along with sneakers, you want to exchange the purifier to large size and night mode, but still with HEPA filter.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W4219264",
                    "address1": "144 Lakeview Drive",
                    "address2": "Suite 925",
                    "city": "New York",
                    "country": "USA",
                    "state": "NY",
                    "zip": "10228",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4219264",
                    "item_ids": ["8886009523"],
                    "new_item_ids": ["2407258246"],
                    "payment_method_id": "credit_card_1620755",
                },
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3445693",
                    "item_ids": ["6341716129"],
                    "new_item_ids": ["8302289002"],
                    "payment_method_id": "credit_card_1620755",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="o32",
        instruction="Your name is User o32 and your email is user.o32@example.com. You want to return the bookshelf and jigsaw puzzle you received in the same order. Make sure you mention at the beginning that you want to cancel these two things, and that they are from the same order. You also want to return the backpack you received with the vacuum cleaner. You also want to change your pending order address to the default Chicago one, and change the item color to red. You want to get the tracking number of your cancelled order.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W6239298",
                    "item_ids": ["4900661478", "3614853563"],
                    "payment_method_id": "credit_card_2112420",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9218746",
                    "item_ids": ["7824298782"],
                    "payment_method_id": "credit_card_2112420",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W4860251",
                    "address1": "921 Park Avenue",
                    "address2": "Suite 892",
                    "city": "Chicago",
                    "country": "USA",
                    "state": "IL",
                    "zip": "60612",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4860251",
                    "item_ids": ["5209958006"],
                    "new_item_ids": ["8964750292"],
                    "payment_method_id": "credit_card_2112420",
                },
            ),
        ],
        outputs=['286422338955'],
    ),
    Task(
        annotator="0",
        user_id="o32",
        instruction="Your name is User o32 and your email is user.o32@example.com. You want to return the bookshelf and jigsaw puzzle you received in different orders. Make sure you mention at the beginning that you want to cancel these two things, and they are from different orders. You also want to return the backpack you received with the vacuum cleaner. You also want to change your pending order item to red, and address to your default Chicago home (you won't reveal it for private reasons but it's in your profile). You want to get the tracking number of your cancelled order.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W8660475",
                    "item_ids": ["8479046075"],
                    "payment_method_id": "credit_card_2112420",
                },
            ),
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W9218746",
                    "item_ids": ["7824298782"],
                    "payment_method_id": "credit_card_2112420",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W4860251",
                    "address1": "921 Park Avenue",
                    "address2": "Suite 892",
                    "city": "Chicago",
                    "country": "USA",
                    "state": "IL",
                    "zip": "60612",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W4860251",
                    "item_ids": ["5209958006"],
                    "new_item_ids": ["8964750292"],
                    "payment_method_id": "credit_card_2112420",
                },
            ),
        ],
        outputs=['286422338955'],
    ),
    Task(
        annotator="0",
        user_id="p59",
        instruction="Your name is User p59 and your zip code is 19031. For #W4316152, exchange Tea Kettle {'material': 'glass', 'capacity': '2 liters', 'stovetop compatibility': 'induction'} for {'material': 'ceramic', 'stovetop compatibility': 'gas'}, and exchange Tea Kettle {'material': 'glass', 'capacity': '2 liters', 'stovetop compatibility': 'induction'} for {'capacity': '1.5 liters', 'stovetop compatibility': 'gas'}.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4316152",
                    "item_ids": ["7292993796", "7292993796"],
                    "new_item_ids": ["3761330360", "9647374798"],
                    "payment_method_id": "gift_card_7245904",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="v38",
        instruction="Your name is User v38 and your email is user.v38@example.com. You want to exchange your t-shirt because it is too big; one size smaller would be good. You like the cotten feeling. If multiple colors available, you prefer black.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W3388163",
                    "item_ids": ["9354168549"],
                    "new_item_ids": ["2060066974"],
                    "payment_method_id": "paypal_5334408",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="x25",
        instruction="Your name is User x25 and your zip code is 75284. Your received hiking boots but they seem like they have already been worn. You want to send for a new pair with the same specs. You also want to exchange your jigsaw puzzle to a more fancy theme, with 500 pieces less. But you want to keep the same difficulty level.",
        actions=[
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W1304208",
                    "item_ids": ["1615379700"],
                    "new_item_ids": ["1615379700"],
                    "payment_method_id": "paypal_1679017",
                },
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W8353027",
                    "item_ids": ["6245746168"],
                    "new_item_ids": ["3112842858"],
                    "payment_method_id": "paypal_1679017",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="d22",
        instruction="Your name is User d22 and your zip code is 91455. You want to return everything but the tablet in a recently delivered order. You want to know how much you can get back.",
        actions=[
            Action(
                name="return_delivered_order_items",
                kwargs={
                    "order_id": "#W1679211",
                    "item_ids": ["9612497925", "7127170374", "6268080249"],
                    "payment_method_id": "paypal_3022415",
                },
            ),
        ],
        outputs=['346.93'],
    ),
    Task(
        annotator="0",
        user_id="u68",
        instruction="Your name is User u68 and your email is user.u68@example.com. You live on Elm Avenue in Houston, and recently you moved to a new house on the same street and bought a luggage set sent to there. But you realize you have another order sent to the old address, and you want to change your old address to the new home, and change your user default address to the new home. You do not want to reveal your address but the agent should be able to look it up in orders. You also want to exchange your tablet to the cheapest one due to moving costs. Make sure to mention the two address changes then the exchange.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W1603792",
                    "address1": "592 Elm Avenue",
                    "address2": "Suite 978",
                    "city": "Houston",
                    "country": "USA",
                    "state": "TX",
                    "zip": "77242",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "u68",
                    "address1": "592 Elm Avenue",
                    "address2": "Suite 978",
                    "city": "Houston",
                    "country": "USA",
                    "state": "TX",
                    "zip": "77242",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W1603792",
                    "item_ids": ["6501071631"],
                    "new_item_ids": ["2106335193"],
                    "payment_method_id": "credit_card_5694100",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="u68",
        instruction="Your name is User u68 and your email is user.u68@example.com. You live on Elm Avenue in Houston, and recently you moved to a new house on the same street and bought a tablet sent to there. But you realize you have another order sent to the old address, and you want to change your old order address to the new home, and also your user default address to the new home. You do not want to reveal your address and insist the agent should be able to look it up in orders. You also want to exchange your tablet to the cheapest one due to moving costs. Make sure to mention the two address changes then the exchange.",
        actions=[
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W1092119",
                    "address1": "760 Elm Avenue",
                    "address2": "Suite 564",
                    "city": "Houston",
                    "state": "TX", 
                    "country": "USA",
                    "zip": "77034",
                },
            ),
            Action(
                name="modify_user_address",
                kwargs={
                    "user_id": "u68",
                    "address1": "760 Elm Avenue",
                    "address2": "Suite 564",
                    "city": "Houston",
                    "state": "TX",
                    "country": "USA",
                    "zip": "77034",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W1603792",
                    "item_ids": ["6501071631"],
                    "new_item_ids": ["2106335193"],
                    "payment_method_id": "credit_card_5694100",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m52",
        instruction="Your name is User m52 and your zip code is 77159. You want to modify the laptop order to your NYC address (you don't want to reveal it, but it should be in your orders profile). You would also like to modify the laptop to be {'processor': 'i5', 'storage': '256GB SSD', 'color': 'space grey'}. You also want to exchange your watch to have a black dial but keep the leather strap.",
        actions=[
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9810810",
                    "item_ids": ["1355937109"],
                    "new_item_ids": ["9949163720"],
                    "payment_method_id": "gift_card_7252880",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W3730488",
                    "address1": "555 Highland Drive",
                    "address2": "Suite 872",
                    "city": "New York",
                    "country": "USA",
                    "state": "NY",
                    "zip": "10116",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W3730488",
                    "item_ids": ["2913673670"],
                    "new_item_ids": ["2216662955"],
                    "payment_method_id": "gift_card_7252880",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="m52",
        instruction="Your name is User m52 and your zip code is 77159. You want to modify the laptop order to your NYC address (you don't want to reveal it but should be in your orders profile). You would also like to modify the laptop to be 9844888101. You also want to exchange your watch to have a black dial but keep the leather strap.",
        actions=[
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W9810810",
                    "item_ids": ["1355937109"],
                    "new_item_ids": ["9949163720"],
                    "payment_method_id": "gift_card_7252880",
                },
            ),
            Action(
                name="modify_pending_order_address",
                kwargs={
                    "order_id": "#W3730488",
                    "address1": "555 Highland Drive",
                    "address2": "Suite 872",
                    "city": "New York",
                    "country": "USA",
                    "state": "NY",
                    "zip": "10116",
                },
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W3730488",
                    "item_ids": ["2913673670"],
                    "new_item_ids": ["9844888101"],
                    "payment_method_id": "gift_card_7252880",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="j70",
        instruction="Your name is User j70 and your zip code is 85041. You want to cancel all pending orders. You don't want to reveal the reason until the agent asks. You can say ordered by mistake if asked.",
        actions=[
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W5056519", "reason": "ordered by mistake"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W5995614", "reason": "ordered by mistake"},
            ),
        ],
        outputs=[],
    ),
]
