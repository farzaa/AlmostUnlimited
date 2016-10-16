class UserInput:

    def requestUserData(self):
        fileName = raw_input('Enter your video file name to upload\n')
        title = raw_input('Enter a title for this file\n')
        description = raw_input('Enter a description for this video\n')
        #Category with ID 37 correlates with the "People and Blogs" category which we will treat as our default.
        category  = '22'
        #Give keyword 'empty' since our keywords don't matter here.
        keywords = 'empty'
        #Hardcode privacy to unlisted. 
        privacyStatus = 'unlisted'
        return {'fileName': fileName, 'title': title, 'description': description, 'category:': category,
            'keywords': keywords, 'privacyStatus': privacyStatus}







