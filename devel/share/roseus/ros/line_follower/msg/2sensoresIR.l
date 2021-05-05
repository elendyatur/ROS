;; Auto-generated. Do not edit!


(when (boundp 'line_follower::2sensoresIR)
  (if (not (find-package "LINE_FOLLOWER"))
    (make-package "LINE_FOLLOWER"))
  (shadow '2sensoresIR (find-package "LINE_FOLLOWER")))
(unless (find-package "LINE_FOLLOWER::2SENSORESIR")
  (make-package "LINE_FOLLOWER::2SENSORESIR"))

(in-package "ROS")
;;//! \htmlinclude 2sensoresIR.msg.html


(defclass line_follower::2sensoresIR
  :super ros::object
  :slots (_sensor_1 _sensor_2 ))

(defmethod line_follower::2sensoresIR
  (:init
   (&key
    ((:sensor_1 __sensor_1) 0)
    ((:sensor_2 __sensor_2) 0)
    )
   (send-super :init)
   (setq _sensor_1 (round __sensor_1))
   (setq _sensor_2 (round __sensor_2))
   self)
  (:sensor_1
   (&optional __sensor_1)
   (if __sensor_1 (setq _sensor_1 __sensor_1)) _sensor_1)
  (:sensor_2
   (&optional __sensor_2)
   (if __sensor_2 (setq _sensor_2 __sensor_2)) _sensor_2)
  (:serialization-length
   ()
   (+
    ;; int8 _sensor_1
    1
    ;; int8 _sensor_2
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _sensor_1
       (write-byte _sensor_1 s)
     ;; int8 _sensor_2
       (write-byte _sensor_2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _sensor_1
     (setq _sensor_1 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _sensor_1 127) (setq _sensor_1 (- _sensor_1 256)))
   ;; int8 _sensor_2
     (setq _sensor_2 (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _sensor_2 127) (setq _sensor_2 (- _sensor_2 256)))
   ;;
   self)
  )

(setf (get line_follower::2sensoresIR :md5sum-) "5e0a028753b9e2df8eddfa1f654b5f64")
(setf (get line_follower::2sensoresIR :datatype-) "line_follower/2sensoresIR")
(setf (get line_follower::2sensoresIR :definition-)
      "int8 sensor_1
int8 sensor_2

")



(provide :line_follower/2sensoresIR "5e0a028753b9e2df8eddfa1f654b5f64")


