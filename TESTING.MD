<h1> Manual testing </h1>
I manually tested each page and feature to enaure functionality worked. 
| Testcase                                                                     | Expected Result                                                                                             | Test Result |                                                                    |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------       |
| **Homepage -API**                                   |                                                             |             |
| *Root Route*                                 |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET / Unauthenticated                      | 200 Ok - Welcome message displayed.                                    | Pass✅       |
| GET / Authenticated                        | 200 Ok - Welcome message displayed.                                     | Pass✅       |
| *Logout Route*                               |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| POST /dj-rest-auth/logout/ Unauthenticated | 200 - Ok.                       | Pass✅       |
| POST /dj-rest-auth/logout/ Authenticated   | 200 - Ok.                          | Pass✅       |
|                                            |                                                             |             |
| **PROFILES APP**                               |                                                             |             |
| *Profile List*                               |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /profiles/ Unauthenticated             | 200 - Ok  List of profiles displayed.                               | Pass✅       |
| GET /profiles/ Authenticated               | 200 - Ok  List of profiles displayed.                                | Pass✅       |
|                                            |                                                             |             |
| *Profile Detail*                            |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /profiles/<id>/ Unauthenticated        | 200 - Ok  Details of the profile id.                | Pass✅       |
| GET /profiles/<id>/ Authenticated          | 200 - Ok  Details of the profile id.                | Pass✅       |
| PUT /profiles/<id>/ Owner                  | 200 - Ok  Profile has been updated.                                     | Pass✅       |
| PUT /profiles/<id>/ Not Owner              | 403 - Forbidden, user not authorized to update.                | Pass✅       |
| PUT /profiles/<id>/ Unauthenticated        | 403 - Forbidden, user not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| **POSTS APP**                                  |                                                             |             |
| *Post List*                                  |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /posts/ Unauthenticated                | 200 - Ok: All posts listed.                                  | Pass✅       |
| GET /posts/ Authenticated                  | 200 - Ok: All posts listed.                                   | Pass✅       |
| POST /posts/ Authenticated                 | 201 - New post created.                               | Pass✅       |
| POST /posts/ Unauthenticated               | 403 - Forbidden, This user is not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| *Post Detail*                                |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /posts/<id>/ Unauthenticated           | 200 - Ok: Details of the post and id.                   | Pass✅       |
| GET /posts/<id>/ Authenticated             | 200 - Ok: Details of the post and id.                   | Pass✅       |
| PUT /posts/<id>/ Owner                     | 200 - Ok: Post is updated.                                        | Pass✅       |
| PUT /posts/<id>/ Not Owner                 | 403 - Forbidden: This user is not authorized to update.                | Pass✅       |
| PUT /posts/<id>/ Unauthenticated           | 403 - Forbidden: This user is not authenticated.                       | Pass✅       |
| DELETE /posts/<id>/ Owner                  | 204 - No Content: The post is deleted.                                | Pass✅       |
| DELETE /posts/<id>/ Not Owner              | 403 - Forbidden: This user is not authorized to delete.                | Pass✅       |
| DELETE /posts/<id>/ Unauthenticated        | 403 - Forbidden: This user is not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| **COMMENT APP**                                |                                                             |             |
| *Comment List*                               |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /comments/ Unauthenticated             | 200 - Ok: Displays a list of all comments.                                | Pass✅       |
| GET /comments/ Authenticated               | 200 - Ok: Displays a list of all comments.                                  | Pass✅       |
| POST /comments/ Authenticated              | 201-  Created: A new comment created.                            | Pass✅       |
| POST /comments/ Unauthenticated            | 403 - Forbidden: This user is not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| *Comment Detail*                             |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /comments/<id>/ Unauthenticated        | 200 - Ok: Details of the comment and id.                | Pass✅       |
| GET /comments/<id>/ Authenticated          | 200 - Ok: Details of the comment and id.                | Pass✅       |
| PUT /comments/<id>/ Owner                  | 200 - Ok: Comment is updated.                                     | Pass✅       |
| PUT /comments/<id>/ Not Owner              | 403 - Forbidden: uThis user is not authorized to update.                | Pass✅       |
| PUT /comments/<id>/ Unauthenticated        | 403 - Forbidden: This user is not authenticated.                       | Pass✅       |
| DELETE /comments/<id>/ Owner               | 204 - No Content: Comment deleted.                             | Pass✅       |
| DELETE /comments/<id>/ Not Owner           | 403 - Forbidden: This user is not authorized to delete.                | Pass✅       |
| DELETE /comments/<id>/ Unauthenticated     | 403 - Forbidden: The user not authenticated.                      | Pass✅       |
|                                            |                                                             |             |
| **LIKES APP**                                  |                                                             |             |
| *Like List*                                  |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /likes/ Unauthenticated                | 200 - Ok: Displays a list of all likes.                                   | Pass✅       |
| GET /likes/ Authenticated                  | 200 - Ok: Displays a list of all likes.                                   | Pass✅       |
| POST /likes/ Authenticated                 | 201 - Created: A new like created.                              | Pass✅       |
| POST /likes/ Unauthenticated               | 403 - Forbidden: The user not authenticated.                      | Pass✅       |
|                                            |                                                             |             |
| *Like Detail*                                |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /likes/<id>/ Unauthenticated           | 200 - Ok: Details of the like and id.                  | Pass✅       |
| GET /likes/<id>/ Authenticated             | 200 - Ok: Details of the like and id.                  | Pass✅       |
| DELETE /likes/<id>/ Owner                  | 204 No Content, like deleted                                | Pass✅       |
| DELETE /likes/<id>/ Not Owner              | 403 - Forbidden: This user is not authorized to delete.                | Pass✅       |
| DELETE /likes/<id>/ Unauthenticated        | 403 - Forbidden: The user not authenticated.                      | Pass✅       |
|                                            |                                                             |             |
| *Liked Posts*                                |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /liked-posts/ Authenticated            | 200 - Ok: Displays a list of posts liked by the authenticated user.       | Pass✅       |
| GET /liked-posts/ Unauthenticated          | 403 - Forbidden: The user is not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| **FOLLOWERS APP**                              |                                                             |             |
| *Follower List*                              |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /followers/ Unauthenticated            | 200 - Ok: Displays list of all follower relationships.                  | Pass✅       |
| GET /followers/ Authenticated              | 200 - Ok: Displays list of all follower relationships.                  | Pass✅       |
| POST /followers/ Authenticated             | 201 - Created: A new follower relationship has been created.              | Pass✅       |
| POST /followers/ Unauthenticated           | 403 - Forbidden: The user not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| *Follower Detail*                            |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /followers/<id>/ Unauthenticated       | 200 - Ok: Details of the follower relationship and id.  | Pass✅       |
| GET /followers/<id>/ Authenticated         | 200 - Ok: Details of the follower relationship and id.  | Pass✅       |
| DELETE /followers/<id>/ Owner              | 204 - No Content: Relationship deleted.               | Pass✅       |
| DELETE /followers/<id>/ Not Owner          | 403 - Forbidden: This user is not authorized to delete.                | Pass✅       |
| DELETE /followers/<id>/ Unauthenticated    | 403 - Forbidden: The user not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| *Followed Posts*                             |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /followed-posts/ Authenticated         | 200 - Ok: Displays list of all posts from followed users.                   | Pass✅       |
| GET /followed-posts/ Unauthenticated       | 403 - Forbidden: The user not authenticated.                       | Pass✅       |
|                                                                                                  
| **CATEGORY APP**                               |                                                             |             |
| *Category List*                              |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /category/ Unauthenticated             | 200 - Ok: Displays list of all categories.                              | Pass✅       |
| GET /category/ Authenticated               | 200 - Ok: Displays list of all categories.                             | Pass✅       |
| POST /category/ Authenticated              | 201 - Created: A new category created.                           | Pass✅       |
| POST /category/ Unauthenticated            | 403 - Forbidden: The user not authenticated.                      | Pass✅       |
|                                            |                                                             |             |
| *Category Detail*                            |                                                           |             |
| **Test**                                   | **Expected Result**                                         | **Test Result** |
| GET /category/<id>/ Unauthenticated        | 200 - Ok: Details of the category and id.               | Pass✅       |
| GET /category/<id>/ Authenticated          | 200 - Ok: Details of the category and id.               | Pass✅       |
| PUT /category/<id>/ Owner                  | 200 - Ok: The category is updated.                                    | Pass✅       |
| PUT /category/<id>/ Not Owner              | 403 - Forbidden: The user is not authorized to update.                | Pass✅       |
| PUT /category/<id>/ Unauthenticated        | 403 - Forbidden: The user not authenticated.                       | Pass✅       |
| DELETE /category/<id>/ Owner               | 204 - No Content: This category is deleted.                           | Pass✅       |
| DELETE /category/<id>/ Not Owner           | 403 - Forbidden: This user is not authorized to delete.                | Pass✅       |
| DELETE /category/<id>/ Unauthenticated     | 403 - Forbidden: This user is not authenticated.                       | Pass✅       |
|                                            |                                                             |             |
| **CONTACT APP**                            |                                                             |             |
| *Contact List*                             |                                                             |             |
| **Test**                                   | **Expected Result**                                         | **Test Result** |
| GET /contact                               | 200 - Ok: Returns a list of all messages.                       | Pass✅       |
|
|                                            |                                                             |             |
| *Contact Detail*                            |                                                             |             |
| **Test**                                   | **Expected Result**                                             | **Test Result** |
| GET /contact/<id>/                        | Returns the contact details.                                  | Pass✅       |
| PUT /contact/<id>/ Not Owner              | 403 - Forbidden: This user is not authorized to update.                | Pass✅       |
| DELETE /contact/<id>/ Not Owner           | 403 - Forbidden: This user is not authorized to delete.                | Pass✅       |
| DELETE /contact/<id>/ Unauthenticated     | 403 - Forbidden: This user is not authenticated.                       | Pass✅       |
|                                            |          