const express = require('express');

exports.get_data = (req,res)=>{
    const beh = req.body;
    console.log(beh);
    res.send('Data recieved');

};

