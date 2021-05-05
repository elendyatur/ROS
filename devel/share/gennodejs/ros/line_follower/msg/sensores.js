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

class sensores {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.IR_1 = null;
      this.IR_2 = null;
      this.US_1 = null;
    }
    else {
      if (initObj.hasOwnProperty('IR_1')) {
        this.IR_1 = initObj.IR_1
      }
      else {
        this.IR_1 = 0;
      }
      if (initObj.hasOwnProperty('IR_2')) {
        this.IR_2 = initObj.IR_2
      }
      else {
        this.IR_2 = 0;
      }
      if (initObj.hasOwnProperty('US_1')) {
        this.US_1 = initObj.US_1
      }
      else {
        this.US_1 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sensores
    // Serialize message field [IR_1]
    bufferOffset = _serializer.int8(obj.IR_1, buffer, bufferOffset);
    // Serialize message field [IR_2]
    bufferOffset = _serializer.int8(obj.IR_2, buffer, bufferOffset);
    // Serialize message field [US_1]
    bufferOffset = _serializer.float32(obj.US_1, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sensores
    let len;
    let data = new sensores(null);
    // Deserialize message field [IR_1]
    data.IR_1 = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [IR_2]
    data.IR_2 = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [US_1]
    data.US_1 = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'line_follower/sensores';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '37c5405c247030f98d7b9d9315f2b46d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #fieldtype1 fieldname1
    #
    int8 IR_1
    int8 IR_2
    float32 US_1
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sensores(null);
    if (msg.IR_1 !== undefined) {
      resolved.IR_1 = msg.IR_1;
    }
    else {
      resolved.IR_1 = 0
    }

    if (msg.IR_2 !== undefined) {
      resolved.IR_2 = msg.IR_2;
    }
    else {
      resolved.IR_2 = 0
    }

    if (msg.US_1 !== undefined) {
      resolved.US_1 = msg.US_1;
    }
    else {
      resolved.US_1 = 0.0
    }

    return resolved;
    }
};

module.exports = sensores;
