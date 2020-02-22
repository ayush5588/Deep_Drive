const express = require('express');
const router = express.Router();
const controller = require('./controller');


router.post('/data',controller.get_data);
router.post('/sensor',controller.xml_data);
module.exports = router;
