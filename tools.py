import json


def print_json(data):
    print("====================================================================================")
    print("====================================================================================")
    print(json.dumps(data, indent=6))
    print("====================================================================================")
    print("====================================================================================")


def data_set(data):
    if (data["eventType"] == "workitem.created"):
        new2 = {"eventType": data["eventType"],
                "workItemId": data["resource"]["id"],
                "Project Name": data["resource"]["fields"]["System.AreaPath"],
                "Title": data["resource"]["fields"]["System.Title"],
                "WorkItemType": data["resource"]["fields"]["System.WorkItemType"],
                "State": data["resource"]["fields"]["System.State"],
                "Reason": data["resource"]["fields"]["System.Reason"]}
        if "System.Description" in data["resource"]["fields"]:
            new2["Description"] = data["resource"]["fields"]["System.Description"]
        if "System.History" in data["resource"]["fields"]:
            new2["History"] = data["resource"]["fields"]["System.History"]
    elif (data["eventType"] == "workitem.updated"):
        new2 = {"eventType": data["eventType"],
                "workItemId": data["resource"]["revision"]["id"],
                "Project Name": data["resource"]["revision"]["fields"]["System.AreaPath"],
                "Title": data["resource"]["revision"]["fields"]["System.Title"],
                "WorkItemType": data["resource"]["revision"]["fields"]["System.WorkItemType"],
                "State": data["resource"]["revision"]["fields"]["System.State"],
                "Reason": data["resource"]["revision"]["fields"]["System.Reason"]}
        if "System.Description" in data["resource"]["revision"]["fields"]:
            new2["Description"] = data["resource"]["revision"]["fields"]["System.Description"]
        if "System.History" in data["resource"]["revision"]["fields"]:
            new2["History"] = data["resource"]["revision"]["fields"]["System.History"]
    text = json.dumps(new2, indent=4)
    return text
