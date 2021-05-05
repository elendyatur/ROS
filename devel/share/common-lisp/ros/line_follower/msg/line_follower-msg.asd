
(cl:in-package :asdf)

(defsystem "line_follower-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "dos_sensores_IR" :depends-on ("_package_dos_sensores_IR"))
    (:file "_package_dos_sensores_IR" :depends-on ("_package"))
    (:file "sensores" :depends-on ("_package_sensores"))
    (:file "_package_sensores" :depends-on ("_package"))
  ))