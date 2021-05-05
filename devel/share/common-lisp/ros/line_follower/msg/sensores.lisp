; Auto-generated. Do not edit!


(cl:in-package line_follower-msg)


;//! \htmlinclude sensores.msg.html

(cl:defclass <sensores> (roslisp-msg-protocol:ros-message)
  ((IR_1
    :reader IR_1
    :initarg :IR_1
    :type cl:fixnum
    :initform 0)
   (IR_2
    :reader IR_2
    :initarg :IR_2
    :type cl:fixnum
    :initform 0)
   (US_1
    :reader US_1
    :initarg :US_1
    :type cl:float
    :initform 0.0))
)

(cl:defclass sensores (<sensores>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sensores>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sensores)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name line_follower-msg:<sensores> is deprecated: use line_follower-msg:sensores instead.")))

(cl:ensure-generic-function 'IR_1-val :lambda-list '(m))
(cl:defmethod IR_1-val ((m <sensores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader line_follower-msg:IR_1-val is deprecated.  Use line_follower-msg:IR_1 instead.")
  (IR_1 m))

(cl:ensure-generic-function 'IR_2-val :lambda-list '(m))
(cl:defmethod IR_2-val ((m <sensores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader line_follower-msg:IR_2-val is deprecated.  Use line_follower-msg:IR_2 instead.")
  (IR_2 m))

(cl:ensure-generic-function 'US_1-val :lambda-list '(m))
(cl:defmethod US_1-val ((m <sensores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader line_follower-msg:US_1-val is deprecated.  Use line_follower-msg:US_1 instead.")
  (US_1 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sensores>) ostream)
  "Serializes a message object of type '<sensores>"
  (cl:let* ((signed (cl:slot-value msg 'IR_1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'IR_2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'US_1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sensores>) istream)
  "Deserializes a message object of type '<sensores>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'IR_1) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'IR_2) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'US_1) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sensores>)))
  "Returns string type for a message object of type '<sensores>"
  "line_follower/sensores")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sensores)))
  "Returns string type for a message object of type 'sensores"
  "line_follower/sensores")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sensores>)))
  "Returns md5sum for a message object of type '<sensores>"
  "37c5405c247030f98d7b9d9315f2b46d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sensores)))
  "Returns md5sum for a message object of type 'sensores"
  "37c5405c247030f98d7b9d9315f2b46d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sensores>)))
  "Returns full string definition for message of type '<sensores>"
  (cl:format cl:nil "#fieldtype1 fieldname1~%#~%int8 IR_1~%int8 IR_2~%float32 US_1~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sensores)))
  "Returns full string definition for message of type 'sensores"
  (cl:format cl:nil "#fieldtype1 fieldname1~%#~%int8 IR_1~%int8 IR_2~%float32 US_1~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sensores>))
  (cl:+ 0
     1
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sensores>))
  "Converts a ROS message object to a list"
  (cl:list 'sensores
    (cl:cons ':IR_1 (IR_1 msg))
    (cl:cons ':IR_2 (IR_2 msg))
    (cl:cons ':US_1 (US_1 msg))
))
