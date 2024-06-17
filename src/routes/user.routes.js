import { Router } from "express";
import { registerUser, loginUser, llmModel, getUserProfile, editUserProfile, aiModel} from "../controllers/user.controller.js";
import { upload } from "../middlewares/multer.middleware.js";

const router = Router()

router.get('/', (req, res) => {
    res.send('Hello world');
});
router.route("/register").post(registerUser)
router.route("/login").post(loginUser)
router.route("/qa").post(aiModel)
router.route("/llm").post(llmModel)
router.route("/profile").get(getUserProfile)

router.route("/edit").post(
    upload.fields([                               //yeh humara middleware hai
        {
            name: "avatar",
            maxCount: 1
        },
        {
            name: "coverImage",
            maxCount: 1
        }
    ]),
    editUserProfile)
export default router