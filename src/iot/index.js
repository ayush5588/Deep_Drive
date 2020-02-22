const express = require('express');
const router = express.Router();
const controller = require('./controller');


router.post('/data',controller.get_data);

module.exports = router;
