key_id="rzp_test_sSj3DF8kI97bSo" 
key_secret="UtzDhOevixD28yF1DyrakRv1"

import razorpay 
client = razorpay.Client(auth=(key_id, key_secret))
# user_name = request.user
# print(user_name)
data = {
'amount': 100*500,
'currency':"BDT",
'receipt': "test_order",
'notes':{
    'user': "user_name",
    }
}
order = client.order.create(data=data)
print(order)


