; Auto-generated. Do not edit!


(cl:in-package line_follower-msg)


;//! \htmlinclude 2sensoresIR.msg.html

(cl:defclass <2sensoresIR> (roslisp-msg-protocol:ros-message)
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

(cl:defclass 2sensoresIR (<2sensoresIR>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <2sensoresIR>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m '2sensoresIR)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name line_follower-msg:<2sensoresIR> is deprecated: use line_follower-msg:2sensoresIR instead.")))

(cl:ensure-generic-function 'sensor_1-val :lambda-list '(m))
(cl:defmethod sensor_1-val ((m <2sensoresIR>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader line_follower-msg:sensor_1-val is deprecated.  Use line_follower-msg:sensor_1 instead.")
  (sensor_1 m))

(cl:ensure-generic-function 'sensor_2-val :lambda-list '(m))
(cl:defmethod sensor_2-val ((m <2sensoresIR>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader line_follower-msg:sensor_2-val is deprecated.  Use line_follower-msg:sensor_2 instead.")
  (sensor_2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <2sensoresIR>) ostream)
  "Serializes a message object of type '<2sensoresIR>"
  (cl:let* ((signed (cl:slot-value msg 'sensor_1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'sensor_2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <2sensoresIR>) istream)
  "Deserializes a message object of type '<2sensoresIR>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sensor_1) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sensor_2) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<2sensoresIR>)))
  "Returns string type for a message object of type '<2sensoresIR>"
  "line_follower/2sensoresIR")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '2sensoresIR)))
  "Returns string type for a message object of type '2sensoresIR"
  "line_follower/2sensoresIR")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<2sensoresIR>)))
  "Returns md5sum for a message object of type '<2sensoresIR>"
  "5e0a028753b9e2df8eddfa1f654b5f64")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '2sensoresIR)))
  "Returns md5sum for a message object of type '2sensoresIR"
  "5e0a028753b9e2df8eddfa1f654b5f64")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<2sensoresIR>)))
  "Returns full string definition for message of type '<2sensoresIR>"
  (cl:format cl:nil "int8 sensor_1~%int8 sensor_2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '2sensoresIR)))
  "Returns full string definition for message of type '2sensoresIR"
  (cl:format cl:nil "int8 sensor_1~%int8 sensor_2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <2sensoresIR>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <2sensoresIR>))
  "Converts a ROS message object to a list"
  (cl:list '2sensoresIR
    (cl:cons ':sensor_1 (sensor_1 msg))
    (cl:cons ':sensor_2 (sensor_2 msg))
))
