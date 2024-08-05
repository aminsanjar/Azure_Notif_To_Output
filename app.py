from flask import Flask, jsonify, request
from send_to_Output import send_notif
import codecs
from tools import data_set, print_json

app = Flask(__name__)


@app.route('/output_notif', methods=['POST'])
def receive_post_data():
    print("\n\n\n\n\n\n================================ New request ================================")
    data = request.get_json()
    # print_json(data)
    user = None
    user_name = "sanjarmoosavi-m"
    project = "نا معلوم"
    workItemId = "0"
    LINK = "این پیام به علت نقص در پارامتر ها برای شما ارسال شد"
    if ("eventType" in data):
        if (data["eventType"] == "workitem.created"):
            if ("System.AssignedTo" in data["resource"]["fields"]):
                user = data["resource"]["fields"]["System.AssignedTo"]["uniqueName"].replace(
                    "BST\\", "")
                user_name = data["resource"]["fields"]["System.AssignedTo"]["displayName"]
                LINK = data["resource"]["_links"]["self"]["href"]
                project = data["resource"]["fields"]["System.AreaPath"]
                workItemId = data["resource"]["id"]
            else:
                print('This request is not the north parameter of "AssignedTo"!!!')
                # return jsonify({"successfully": False, "message": "e1"})
        elif (data["eventType"] == "workitem.updated"):
            if ("System.AssignedTo" in data["resource"]["revision"]["fields"]):
                user = data["resource"]["revision"]["fields"]["System.AssignedTo"]["uniqueName"].replace(
                    "BST\\", "")
                user_name = data["resource"]["revision"]["fields"]["System.AssignedTo"]["displayName"]
                LINK = data["resource"]["revision"]["_links"]["self"]["href"]
                project = data["resource"]["revision"]["fields"]["System.AreaPath"]
                workItemId = data["resource"]["revision"]["id"]
            else:
                print('This request is not the north parameter of "AssignedTo"!!!')
                # return jsonify({"successfully": False, "message": "e2"})
    else:
        print('This request is not the north parameter of "eventType"!!!')
        return jsonify({"successfully": False, "message": "e3"})

    if ("resourceContainers" in data and "collection" in data["resourceContainers"] and "baseUrl" in data["resourceContainers"]["collection"]):
        LINK = data["resourceContainers"]["collection"]["baseUrl"] + \
            "/"+project + "/_workitems/edit/" + str(workItemId)
        LINK = LINK.replace("srv-azure", "192.168.160.33")

    msg = "تسک با مشخصات زير به شما ارجاع داده شد"
    return send_notif(user, user_name + ' عزيز '+'\n'+msg + '\n <p dir="ltr" style="text-align: left">' +
                      codecs.decode(data_set(data), "unicode-escape")+'</p>\n' + '\n'+'<a href="'+LINK+'">مشاهده تسک</a>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=5000)
