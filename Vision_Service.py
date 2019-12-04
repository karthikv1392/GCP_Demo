_Author_ = "Karthik Vaidhyanathan"
# Web service file of the ArchLearner backend

import tornado.web
from tornado.options import define, options
import tornado.httpserver
import tornado.ioloop
from Initializer import Initialize
#from Custom_Logger import logger
import json
from tornado.escape import json_encode
import os
import requests


from configparser import ConfigParser

import traceback
import base64

init_object = Initialize()

class Google_Vision_Connector():

    def fetch_image_analytics(self,image_path):
        return_json = {}
        final_request_url = init_object.request_url + "key="+init_object.api_key
        json_data = {}
        list_contents = []
        features_list = []
        feature_dict = {}
        feature_dict["type"] = "LABEL_DETECTION"
        feature_dict["maxResults"] = 10
        features_list.append(feature_dict)
        content_dict = {}
        image_dict = {}
        encoded_image = ""
        with open(image_path, "rb") as img_file:
            encoded_image= base64.b64encode(img_file.read())
        encoded_image = str(encoded_image).strip("b'")
        image_dict["content"] = encoded_image
        content_dict["image"] = image_dict
        content_dict["features"] = features_list
        list_contents.append(content_dict)

        json_data["requests"] = list_contents
        json_data = json.dumps(json_data)
        print (final_request_url)
        print (json_data)
        response = requests.post(final_request_url, json_data)
        # print response
        #logger.info("Obtainted the encoded image")
        response_json = json.loads(response.text)
        print (response_json)
        raw_text = response_json["responses"][0]["labelAnnotations"]
        print (raw_text)
        response_json = {}
        response_json["response"] = raw_text
        return  response_json


google_vision_obj = Google_Vision_Connector()

class Analyze_Image_Service(tornado.web.RequestHandler):
    def post(self):
        response_json = {}
        response_json["status"] = "Failed"
        # response_json["invoiceAmount"] = "Parsing Failed"
        self.set_header('Access-Control-Allow-Origin', '*')
        try:
            #logger.info("Inside the pdf extract all fields handler")
            file_name = "upload.jpg"
            upload_path = init_object.upload_path
            # fileinfo = self.request.files['filearg'].save(upload_path + file_name)
            fileinfo = self.request.files['filearg'][0]
            print (fileinfo)
            fname = fileinfo['filename']
            #logger.info(" Obtained file name " + str(fname))
            print (fname)
            fh = open(upload_path + file_name, 'wb')
            fh.write(fileinfo['body'])
            fh.close()
            #logger.info("file upload successfull")
            full_file_name = init_object.upload_path + file_name
            if os.path.exists(full_file_name):
                print (full_file_name)
                response_json = google_vision_obj.fetch_image_analytics(full_file_name)
                os.remove(full_file_name)
                response_json["status"] = "success"
                #logger.info("file deleted successfully")
            else:
                #logger.info("no such files")
                response_json["status"] = "failed"
                # response_json["invoiceAmount"] = "no such file exists"
            self.write(json_encode(response_json))
        except:
            traceback.print_exc()
            #logger.error("Error in processing the file")
            self.write(json_encode(response_json))




class Application(tornado.web.Application):
    def __init__(self):
        try:
            handlers = [
                (r"/analyze",Analyze_Image_Service),
            ]
            tornado.web.Application.__init__(self, handlers)
        except:
            print ("Exception occurred when initializing Application")
            print (traceback.format_exc())

def main():
    try:
        print ("Starting Tornado Web Server on " + str(init_object.port))
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.listen(init_object.port)
        tornado.ioloop.IOLoop.instance().start()
    except:
        #logger.exception( "Exception occurred when trying to start tornado on " + str(options.port))
        traceback.print_exc()

if __name__ == "__main__":
    main()


