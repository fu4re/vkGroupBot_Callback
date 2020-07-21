import vk_api
import httplib2

from vk_api.utils import get_random_id

from settings import *

vk_session = vk_api.VkApi(token=API_TOKEN)
api = vk_session.get_api()
upload = vk_api.VkUpload(vk_session)



def sendMessage(user_id, message, attachment=None):
    api.messages.send(user_id=user_id,
                      random_id=get_random_id(),
                      message=message,
                      attachment=attachment
                      )


def get_random_wall_picture(group_id):
    h = httplib2.Http('.cache')
    response, content = h.request(img)
    out = open('...\img.jpg', 'wb')
    out.write(content)
    out.close()

    return content




