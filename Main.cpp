#include <Siv3D.hpp>
#include <HamFramework.hpp>

//PCの内蔵カメラで顔が映っているかを検出する。写ってたらTrueを返す。
bool isFace(){
    Webcam webcam(0);
    if (!webcam.start()){
        return;
    }
    Image image;
    DynamicTexture texture;
    while (System::Update()){
        if (webcam.hasNewFrame()){
            webcam.getFrame(image);
            for (const auto rect : Imaging::DetectFaces(image, CascadeType::Photo, 3, { 40, 40 })){
                return True;
            }
            texture.fill(image);
        }
        if (texture){
            texture.mirror().draw();
        }
    }
}

void Main(){

}
