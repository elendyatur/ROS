// Auto-generated. Do not edit!

// (in-package line_follower.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class dos_sensores_IR {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sensor_1 = null;
      this.sensor_2 = null;
    }
    else {
      if (initObj.hasOwnProperty('sensor_1')) {
        this.sensor_1 = initObj.sensor_1
      }
      else {
        this.sensor_1 = 0;
      }
      if (initObj.hasOwnProperty('sensor_2')) {
        this.sensor_2 = initObj.sensor_2
      }
      else {
        this.sensor_2 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type dos_sensores_IR
    // Serialize message field [sensor_1]
    bufferOffset = _serializer.int8(obj.sensor_1, buffer, bufferOffset);
    // Serialize message field [sensor_2]
    bufferOffset = _serializer.int8(obj.sensor_2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type dos_sensores_IR
    let len;
    let data = new dos_sensores_IR(null);
    // Deserialize message field [sensor_1]
    data.sensor_1 = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [sensor_2]
    data.sensor_2 = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'line_follower/dos_sensores_IR';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5e0a028753b9e2df8eddfa1f654b5f64';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #fieldtype1 fieldname1
    #
    int8 sensor_1
    int8 sensor_2
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new dos_sensores_IR(null);
    if (msg.sensor_1 !== undefined) {
      resolved.sensor_1 = msg.sensor_1;
    }
    else {
      resolved.sensor_1 = 0
    }

    if (msg.sensor_2 !== undefined) {
      resolved.sensor_2 = msg.sensor_2;
    }
    else {
      resolved.sensor_2 = 0
    }

    return resolved;
    }
};

module.exports = dos_sensores_IR;
