from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credentials.json")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    gauth.SaveCredentialsFile("credentials.json")
    return GoogleDrive(gauth)


def get_latest_txt_file(drive, folder_name):
    folder_id = get_folder_id(drive, folder_name)
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and mimeType='text/plain' and trashed=false"}).GetList()
    if not file_list:
        return None, None

    file_data_list = []
    for file in file_list:
        file_content = file.GetContentString()
        file_data_list.append([file_content, file])

    return file_data_list


def get_folder_id(drive, folder_name):
    folders = drive.ListFile({'q': "mimeType='application/vnd.google-apps.folder'"}).GetList()
    for folder in folders:
        if folder['title'] == folder_name:
            return folder['id']
    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    return folder['id']
