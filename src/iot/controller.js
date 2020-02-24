const xmlToJson = require('xml-to-json-stream');
const parser = xmlToJson({attributeMode: false});
const fs = require('fs');
let writeStream = fs.createWriteStream('behaviour.txt');

const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const csvWriter = createCsvWriter({
    path: './iot.csv',
    header: [
      {id: 'a1', title: 'A1'},
      {id: 'a2', title: 'A2'},
      {id: 'a3', title: 'A3'},
      {id: 'g1', title: 'G1'},
      {id: 'g2', title: 'G2'},
      {id: 'g3', title: 'G3'}
    ]
  });



exports.get_data = (req,res)=>{
    
    
    const data = req.body.Behaviour;
    writeStream.write(data,(e)=>{
        if(e){
            throw e;
        }else{
            console.log('Data written in file');
            res.send('data received at route->1');
        }
        
    
    });
    

    


};

exports.xml_data = (req,res)=>{

    var xml = req.body.Sensor;
    parser.xmlToJson(xml,(e,result)=>{
        if(e){
            console.log(e);
        }else{
            
            var obj = {};
            const a1 = result.Accelerometer.Accelerometer1;
            const a2 = result.Accelerometer.Accelerometer2;
            const a3 = result.Accelerometer.Accelerometer3;

            const g1 = result.Gyroscope.Gyroscope1;
            const g2 = result.Gyroscope.Gyroscope2;
            const g3 = result.Gyroscope.Gyroscope3;

            obj.a1 = a1;
            obj.a2 = a2;
            obj.a3 = a3;
            obj.g1 = g1;
            obj.g2 = g2;
            obj.g3 = g3;
            //console.log(obj);
            var array = [];
            array.push(obj);
            
            csvWriter
            .writeRecords(array)
            .then(()=> console.log('The CSV file was written successfully'));
            res.send('Data recieved route-2');    
        }
        
    });
    
}