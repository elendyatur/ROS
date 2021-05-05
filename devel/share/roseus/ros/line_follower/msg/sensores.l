;; Auto-generated. Do not edit!


(when (boundp 'line_follower::sensores)
  (if (not (find-package "LINE_FOLLOWER"))
    (make-package "LINE_FOLLOWER"))
  (shadow 'sensores (find-package "LINE_FOLLOWER")))
(unless (find-package "LINE_FOLLOWER::SENSORES")
  (make-package "LINE_FOLLOWER::SENSORES"))

(in-package "ROS")
;;//! \htmlinclude sensores.msg.html


(defclass line_follower::sensores
  :super ros::object
  :slots (_IR_1 _IR_2 _US_1 ))

(defmethod line_follower::sensores
  (:init
   (&key
    ((:IR_1 __IR_1) 0)
    ((:IR_2 __IR_2) 0)
    ((:US_1 __US_1) 0.0)
    )
   (send-super :init)
   (setq _IR_1 (round __IR_1))
   (setq _IR_2 (round __IR_2))
   (setq _US_1 (float __US_1))
   self)
  (:IR_1
   (&optional __IR_1)
   (if __IR_1 (setq _IR_1 __IR_1)) _IR_1)
  (:IR_2
   (&optional __IR_2)
   (if __IR_2 (setq _IR_2 __IR_2)) _IR_2)
  (:US_1
   (&optional __US_1)
   (if __US_1 (setq _US_1 __US_1)) _US_1)
  (:serialization-length
   ()
   (+
    ;; int8 _IR_1
    1
    ;; int8 _IR_2
    1
    ;; float32 _US_1
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _IR_1
       (write-byte _IR_1 s)
     ;; int8 _IR_2
       (write-byte _IR_2 s)
     ;; float32 _US_1
       (sys::poke _US_1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _IR_1
     (setq _IR_1 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _IR_1 127) (setq _IR_1 (- _IR_1 256)))
   ;; int8 _IR_2
     (setq _IR_2 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _IR_2 127) (setq _IR_2 (- _IR_2 256)))
   ;; float32 _US_1
     (setq _US_1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get line_follower::sensores :md5sum-) "37c5405c247030f98d7b9d9315f2b46d")
(setf (get line_follower::sensores :datatype-) "line_follower/sensores")
(setf (get line_follower::sensores :definition-)
      "#fieldtype1 fieldname1
#
int8 IR_1
int8 IR_2
float32 US_1
")



(provide :line_follower/sensores "37c5405c247030f98d7b9d9315f2b46d")


