#######################################################
import uuid ## random id generator
from streamlit_option_menu import option_menu
from settings import *
#######################################################
## Disable Warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)
################################################### Defining Static Data ###############################################
st.sidebar.image('https://th.bing.com/th/id/OIP.FgvEBXnKfDC1yltDsFjEXAHaGa?r=0&rs=1&pid=ImgDetMain',
                 use_column_width=False)
st.sidebar.markdown("""
                    > Made by [*YP18*](https://github.com/alesandroyoel)
                    """)

user_color      = '#000000'
title_webapp    = "Visitor Monitoring Webapp"
image_link      = "data:image/jpeg;base64,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"

html_temp = f"""
            <div style="background-color:{user_color};padding:12px">
            <h1 style="color:white;text-align:center;">{title_webapp}
            <img src = "{image_link}" align="right" width=150px ></h1>
            </div>
            """
st.markdown(html_temp, unsafe_allow_html=True)

###################### Defining Static Paths ###################4
if st.sidebar.button('Click to Clear out all the data'):
    ## Clearing Visitor Database
    shutil.rmtree(VISITOR_DB, ignore_errors=True)
    os.mkdir(VISITOR_DB)
    ## Clearing Visitor History
    shutil.rmtree(VISITOR_HISTORY, ignore_errors=True)
    os.mkdir(VISITOR_HISTORY)

if not os.path.exists(VISITOR_DB):
    os.mkdir(VISITOR_DB)

if not os.path.exists(VISITOR_HISTORY):
    os.mkdir(VISITOR_HISTORY)
# st.write(VISITOR_HISTORY)
########################################################################################################################
def main():
    ###################################################
    st.sidebar.header("About")
    st.sidebar.info("This webapp gives a demo of Visitor Monitoring "
                    "Webapp using 'Face Recognition' and Streamlit")
    ###################################################

    selected_menu = option_menu(None,
        ['Visitor Validation', 'View Visitor History', 'Add to Database'],
        icons=['camera', "clock-history", 'person-plus'],
        ## icons from website: https://icons.getbootstrap.com/
        menu_icon="cast", default_index=0, orientation="horizontal")

    if selected_menu == 'Visitor Validation':
        ## Generates a Random ID for image storage
        visitor_id = uuid.uuid1()

        ## Reading Camera Image
        img_file_buffer = st.camera_input("Take a picture")

        if img_file_buffer is not None:
            bytes_data = img_file_buffer.getvalue()

            # convert image from opened file to np.array
            image_array         = cv2.imdecode(np.frombuffer(bytes_data,
                                                             np.uint8),
                                               cv2.IMREAD_COLOR)
            image_array_copy    = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            # st.image(cv2_img)

            ## Saving Visitor History
            with open(os.path.join(VISITOR_HISTORY,
                                   f'{visitor_id}.jpg'), 'wb') as file:
                file.write(img_file_buffer.getbuffer())
                st.success('Image Saved Successfully!')

                ## Validating Image
                # Detect faces in the loaded image
                max_faces   = 0
                rois        = []  # region of interests (arrays of face areas)

                ## To get location of Face from Image
                face_locations  = face_recognition.face_locations(image_array)
                ## To encode Image to numeric format
                encodesCurFrame = face_recognition.face_encodings(image_array,
                                                                  face_locations)

                ## Generating Rectangle Red box over the Image
                for idx, (top, right, bottom, left) in enumerate(face_locations):
                    # Save face's Region of Interest
                    rois.append(image_array[top:bottom, left:right].copy())

                    # Draw a box around the face and label it
                    cv2.rectangle(image_array, (left, top), (right, bottom), COLOR_DARK, 2)
                    cv2.rectangle(image_array, (left, bottom + 35), (right, bottom), COLOR_DARK, cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(image_array, f"#{idx}", (left + 5, bottom + 25), font, .55, COLOR_WHITE, 1)

                ## Showing Image
                st.image(BGR_to_RGB(image_array), width=720)

                ## Number of Faces identified
                max_faces = len(face_locations)

                if max_faces > 0:
                    col1, col2 = st.columns(2)

                    # select selected faces in the picture
                    face_idxs = col1.multiselect("Select face#", range(max_faces),
                                                 default=range(max_faces))

                    ## Filtering for similarity beyond threshold
                    similarity_threshold = col2.slider('Select Threshold for Similarity',
                                                         min_value=0.0, max_value=1.0,
                                                         value=0.5)
                                                    ## check for similarity confidence greater than this threshold

                    flag_show = False

                    if ((col1.checkbox('Click to proceed!')) & (len(face_idxs)>0)):
                        dataframe_new = pd.DataFrame()

                        ## Iterating faces one by one
                        for face_idx in face_idxs:
                            ## Getting Region of Interest for that Face
                            roi = rois[face_idx]
                            # st.image(BGR_to_RGB(roi), width=min(roi.shape[0], 300))

                            # initial database for known faces
                            database_data = initialize_data()
                            # st.write(DB)

                            ## Getting Available information from Database
                            face_encodings  = database_data[COLS_ENCODE].values
                            dataframe       = database_data[COLS_INFO]

                            # Comparing ROI to the faces available in database and finding distances and similarities
                            faces = face_recognition.face_encodings(roi)
                            # st.write(faces)

                            if len(faces) < 1:
                                ## Face could not be processed
                                st.error(f'Please Try Again for face#{face_idx}!')
                            else:
                                face_to_compare = faces[0]
                                ## Comparing Face with available information from database
                                dataframe['distance'] = face_recognition.face_distance(face_encodings,
                                                                                       face_to_compare)
                                dataframe['distance'] = dataframe['distance'].astype(float)

                                dataframe['similarity'] = dataframe.distance.apply(
                                    lambda distance: f"{face_distance_to_conf(distance):0.2}")
                                dataframe['similarity'] = dataframe['similarity'].astype(float)

                                dataframe_new = dataframe.drop_duplicates(keep='first')
                                dataframe_new.reset_index(drop=True, inplace=True)
                                dataframe_new.sort_values(by="similarity", ascending=True)

                                dataframe_new = dataframe_new[dataframe_new['similarity'] > similarity_threshold].head(1)
                                dataframe_new.reset_index(drop=True, inplace=True)

                                if dataframe_new.shape[0]>0:
                                    (top, right, bottom, left) = (face_locations[face_idx])

                                    ## Save Face Region of Interest information to the list
                                    rois.append(image_array_copy[top:bottom, left:right].copy())

                                    # Draw a Rectangle Red box around the face and label it
                                    cv2.rectangle(image_array_copy, (left, top), (right, bottom), COLOR_DARK, 2)
                                    cv2.rectangle(image_array_copy, (left, bottom + 35), (right, bottom), COLOR_DARK, cv2.FILLED)
                                    font = cv2.FONT_HERSHEY_DUPLEX
                                    cv2.putText(image_array_copy, f"#{dataframe_new.loc[0, 'Name']}", (left + 5, bottom + 25), font, .55, COLOR_WHITE, 1)

                                    ## Getting Name of Visitor
                                    name_visitor = dataframe_new.loc[0, 'Name']
                                    attendance(visitor_id, name_visitor)

                                    flag_show = True

                                else:
                                    st.error(f'No Match Found for the given Similarity Threshold! for face#{face_idx}')
                                    st.info('Please Update the database for a new person or click again!')
                                    attendance(visitor_id, 'Unknown')

                        if flag_show == True:
                            st.image(BGR_to_RGB(image_array_copy), width=720)

                else:
                    st.error('No human face detected.')

    if selected_menu == 'View Visitor History':
        view_attendace()

    if selected_menu == 'Add to Database':
        col1, col2, col3 = st.columns(3)

        face_name  = col1.text_input('Name:', '')
        pic_option = col2.radio('Upload Picture',
                                options=["Upload a Picture",
                                         "Click a picture"])

        if pic_option == 'Upload a Picture':
            img_file_buffer = col3.file_uploader('Upload a Picture',
                                                 type=allowed_image_type)
            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                file_bytes = np.asarray(bytearray(img_file_buffer.read()),
                                        dtype=np.uint8)

        elif pic_option == 'Click a picture':
            img_file_buffer = col3.camera_input("Click a picture")
            if img_file_buffer is not None:
                # To read image file buffer with OpenCV:
                file_bytes = np.frombuffer(img_file_buffer.getvalue(),
                                           np.uint8)

        if ((img_file_buffer is not None) & (len(face_name) > 1) &
                st.button('Click to Save!')):
            # convert image from opened file to np.array
            image_array = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            # st.write(image_array)
            # st.image(cv2_img)

            with open(os.path.join(VISITOR_DB,
                                   f'{face_name}.jpg'), 'wb') as file:
                file.write(img_file_buffer.getbuffer())
                # st.success('Image Saved Successfully!')

            face_locations = face_recognition.face_locations(image_array)
            encodesCurFrame = face_recognition.face_encodings(image_array,
                                                              face_locations)

            df_new = pd.DataFrame(data=encodesCurFrame,
                                  columns=COLS_ENCODE)
            df_new[COLS_INFO] = face_name
            df_new = df_new[COLS_INFO + COLS_ENCODE].copy()

            # st.write(df_new)
            # initial database for known faces
            DB = initialize_data()
            add_data_db(df_new)

#######################################################
if __name__ == "__main__":
    main()
#######################################################
