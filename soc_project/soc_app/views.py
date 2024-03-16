from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import requests
from django.http import JsonResponse

count = ''
class TriggerViewSet(viewsets.ViewSet):
    def create(self, request):
        
        if request.method == 'POST':
            global count
            data = request.data
            # print(data.rule_number)
            
            project_id = "19"
            gitlab_token = "glpat-TH-QxA_XxQMeg74xpVrT"

            base_url = f'http://gitlab-ce.os3.com/api/v4/'
            headers = {"PRIVATE-TOKEN": gitlab_token}

            selected_roles = data.get('selectedRules', [])  
            print (selected_roles)
           
            for role in selected_roles:
                branch_name = None
                count=0
                if role == 'rule-1':
                    print("hiirule-1")
                    branch_name = "JUC-1001"
                # 1 rule 01 working   
                elif role == 'rule-20':
                    branch_name = "JUC-1053"

                elif role == 'rule-3':
                    branch_name = "JUC-1004"

                elif role == 'rule-2':
                    branch_name = "JUC-1003"

                elif role == 'rule-10':
                    branch_name = "JUC-1006"

                elif role == 'rule-5':
                    branch_name = "JUC-1008"

                elif role == 'rule-7':
                    branch_name = "JUC-1010"

                elif role == 'rule-17':
                    branch_name = "JUC-1011"

                elif role == 'rule-11':
                    branch_name = "JUC-1012"

                elif role == 'rule-16':
                    branch_name = "JUC-1017"

                elif role == 'rule-19':
                    branch_name = "JUC-1019"

                elif role == 'rule-28':
                    branch_name = "JUC-1027"    

                elif role == 'rule-29':
                    branch_name = "JUC-1028"

                elif role == 'rule-32':
                    branch_name = "JUC-1031" 

                elif role == 'rule-34':
                    branch_name = "JUC-1033"

                elif role == 'rule-42':
                    branch_name = "JUC-1041"

                elif role == 'rule-43':
                    branch_name = "JUC-1042" 

                elif role == 'rule-44':
                    branch_name = "JUC-1043" 
# 2 working 49b
                elif role == 'rule-50':
                    branch_name = "JUC-1049"

                elif role == 'rule-51':
                    branch_name = "JUC-1050" 

                elif role == 'rule-55':
                    branch_name = "JUC-1054"  
# 3 working 55b
                elif role == 'rule-56':
                    branch_name = "JUC-1055"   
# 4 working 62b
                elif role == 'rule-63':
                    branch_name = "JUC-1062" 

                elif role == 'rule-66':
                    branch_name = "JUC-1065"

                elif role == 'rule-67':
                    branch_name = "JUC-1066" 

                elif role == 'rule-27':
                    branch_name = "JUC-1073" 
# 80 not found
                elif role == 'rule-63':
                    branch_name = "JUC-1080"  

                elif role == 'rule-83':
                    branch_name = "JUC-1082"  

                elif role == 'rule-85':
                    branch_name = "JUC-1084"

                elif role == 'rule-87':
                    branch_name = "JUC-1086"

                elif role == 'rule-92':
                    branch_name = "JUC-1091"
#5 working 92b
                elif role == 'rule-93':
                    branch_name = "JUC-1092" 
# no match found after rule93 in db
                elif role == 'rule-63':
                    branch_name = "JUC-1098"   









                     
                count=len(selected_roles)
                if branch_name:
                    print(f'Triggering branch: {branch_name}')
                    print("trigger hiirule-1")
                    trigger_branch(base_url, project_id, headers, branch_name)

            return Response({"message": "pipeline trigger"})
        else:
            return Response({"message": "pipeline not trigger"})


    def get_pipeline_status(self, request):

        project_id = "19"
        gitlab_token = "glpat-TH-QxA_XxQMeg74xpVrT"

        base_url = f'http://gitlab-ce.os3.com/api/v4/'


        headers = {"PRIVATE-TOKEN": gitlab_token}
        pipeline_count = count

        # Get the statuses of the latest pipelines
        latest_pipeline_statuses = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_count)

        # Get the artifacts for each of the latest pipelines
        all_artifacts = []
        for pipeline_status in latest_pipeline_statuses:
            pipeline_id = pipeline_status["id"]
           
            all_artifacts.append({"status": pipeline_status["status"]})

        return JsonResponse({"pipelines": all_artifacts})

  
                 
def trigger_branch(base_url, project_id, headers, branch_name):
        data = {
            "ref": branch_name
            }
        response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)
        print(response.status_code)
        if response.status_code == 201:
            return Response({'message': 'Pipeline triggered successfully.'})
        else:
            return Response({'message': 'Failed to trigger the pipeline.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_latest_pipeline_statuses(base_url, project_id, headers, count=2):
    response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")

    pipelines = response.json()
    if not pipelines:
        return []

    latest_pipelines = pipelines[:count]
    latest_statuses = []

    for pipeline in latest_pipelines:
        latest_status = pipeline['status']
        latest_statuses.append({"id": pipeline['id'], "status": latest_status})

    return latest_statuses