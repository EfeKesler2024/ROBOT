# BYM412 Robotik Dersi Ödev 2

## Proje Özeti
Bu proje, İstanbul Sağlık ve Teknoloji Üniversitesi BYM412 Robotik dersi kapsamında, ROS2 Humble ve Gazebo Harmonic ortamında diferansiyel tahrikli bir robotun sıfırdan tasarlanmasını, kamera sensörü eklenmesini, Ball Chaser algoritmasının geliştirilmesini ve RViz ile doğrulanmasını içerir.

## Klasör Yapısı
- **my_robot_description/**: Robotun URDF/model dosyaları
    - urdf/my_robot.urdf.xacro
- **my_robot_bringup/**: Launch dosyası
    - launch/bringup.launch.py
- **ball_chaser/**: Ball Chaser Python düğümü
    - ball_chaser_node.py
- **SSF_HASH.txt**: SSF çıktısı ve SHA256 hash kanıtı
- **RAPOR.md**: Rapor şablonu

## Kurulum
1. ROS2 Humble ve Gazebo Harmonic kurulu olmalıdır.
2. Gerekli ROS2 paketleri ve Python bağımlılıkları (rclpy, cv_bridge, OpenCV) yüklenmelidir.

## Çalıştırma
Tüm bileşenler tek launch dosyası ile başlatılır:
```bash
ros2 launch my_robot_bringup bringup.launch.py
```
Bu komut ile:
- Gazebo ortamında robot ve beyaz küre başlatılır.
- Kamera görüntüsü /camera/image_raw topicine köprülenir.
- robot_state_publisher ve joint_state_publisher çalışır.
- RViz açılır ve robot modeli ile kamera görüntüsü doğrulanır.
- Ball Chaser düğümü aktif olur.

## Ball Chaser Algoritması
- Girdi: `/camera/image_raw` (sensor_msgs/Image)
- Çıktı: `/cmd_vel` (geometry_msgs/Twist)
- Davranış:
    - Beyaz top görüntünün sağında/solunda ise robot döner.
    - Top merkezde ise robot ileri gider.
    - Top görünmüyorsa robot durur.

## SSF Kanıtı
SSF_HASH.txt dosyasında ssf.sh çıktısı ve SHA256 hash değeri yer alır.

## Rapor
RAPOR.md dosyasında ödev raporunun şablonu ve başlıkları bulunur. PDF olarak doldurulup teslim edilmelidir.

## Katkı ve İletişim
Ad Soyad: EFE EREN KESLER
Okul No: 220609031
E-posta: efe.kesler@istun.edu.tr

## Lisans
Bu proje eğitim amaçlıdır. Tüm kodlar ve dokümanlar bireysel ödev kapsamında hazırlanmıştır.
