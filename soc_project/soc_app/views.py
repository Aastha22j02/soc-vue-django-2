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
            
            project_id = "136"
            gitlab_token = "yMZsychPu_y93N_nMB6Z"

            base_url = f'https://gitlab.os3.com/api/v4/'
            headers = {"PRIVATE-TOKEN": gitlab_token}

            selected_roles = data.get('selectedRules', [])  
            print (selected_roles)
           
            for role in selected_roles:
                branch_name = None
                count=0
                if role == 'rule-1':
                    print("hiirule-1")
                    branch_name = "Detect_unauthorized_access"
                   
                elif role == 'rule-20':
                    branch_name = "Detection_of_account_with_short_lifespan"
                     
                count=len(selected_roles)
                if branch_name:
                    print(f'Triggering branch: {branch_name}')
                    print("trigger hiirule-1")
                    trigger_branch(base_url, project_id, headers, branch_name)

            return Response({"message": "pipeline trigger"})
        else:
            return Response({"message": "pipeline not trigger"})


    def get_pipeline_status(self, request):

        project_id = "136"
        gitlab_token = "yMZsychPu_y93N_nMB6Z"

        base_url = f'https://gitlab.os3.com/api/v4/'


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