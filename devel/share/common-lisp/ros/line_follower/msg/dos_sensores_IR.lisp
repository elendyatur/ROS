; Auto-generated. Do not edit!


(cl:in-package line_follower-msg)


;//! \htmlinclude dos_sensores_IR.msg.html

(cl:defclass <dos_sensores_IR> (roslisp-msg-protocol:ros-message)
  ((sensor_1
    :reader sensor_1
    :initarg :sensor_1
    :type cl:fixnum
    :initform 0)
   (sensor_2
    :reader sensor_2
    :initarg :sensor_2
    :type cl:fixnum
    :initform 0))
)

(cl:defclass dos_sensores_IR (<dos_sensores_IR>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <dos_sensores_IR>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'dos_sensores_IR)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name line_follower-msg:<dos_sensores_IR> is deprecated: use line_follower-msg:dos_sensores_IR instead.")))

(cl:ensure-generic-function 'sensor_1-val :lambda-list '(m))
(cl:defmethod sensor_1-val ((m <dos_sensores_IR>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader line_follower-msg:sensor_1-val is deprecated.  Use line_follower-msg:sensor_1 instead.")
  (sensor_1 m))

(cl:ensure-generic-function 'sensor_2-val :lambda-list '(m))
(cl:defmethod sensor_2-val ((m <dos_sensores_IR>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader line_follower-msg:sensor_2-val is deprecated.  Use line_follower-msg:sensor_2 instead.")
  (sensor_2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <dos_sensores_IR>) ostream)
  "Serializes a message object of type '<dos_sensores_IR>"
  (cl:let* ((signed (cl:slot-value msg 'sensor_1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'sensor_2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <dos_sensores_IR>) istream)
  "Deserializes a message object of type '<dos_sensores_IR>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sensor_1) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sensor_2) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<dos_sensores_IR>)))
  "Returns string type for a message object of type '<dos_sensores_IR>"
  "line_follower/dos_sensores_IR")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'dos_sensores_IR)))
  "Returns string type for a message object of type 'dos_sensores_IR"
  "line_follower/dos_sensores_IR")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<dos_sensores_IR>)))
  "Returns md5sum for a message object of type '<dos_sensores_IR>"
  "5e0a028753b9e2df8eddfa1f654b5f64")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'dos_sensores_IR)))
  "Returns md5sum for a message object of type 'dos_sensores_IR"
  "5e0a028753b9e2df8eddfa1f654b5f64")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<dos_sensores_IR>)))
  "Returns full string definition for message of type '<dos_sensores_IR>"
  (cl:format cl:nil "#fieldtype1 fieldname1~%#~%int8 sensor_1~%int8 sensor_2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'dos_sensores_IR)))
  "Returns full string definition for message of type 'dos_sensores_IR"
  (cl:format cl:nil "#fieldtype1 fieldname1~%#~%int8 sensor_1~%int8 sensor_2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <dos_sensores_IR>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <dos_sensores_IR>))
  "Converts a ROS message object to a list"
  (cl:list 'dos_sensores_IR
    (cl:cons ':sensor_1 (sensor_1 msg))
    (cl:cons ':sensor_2 (sensor_2 msg))
))
