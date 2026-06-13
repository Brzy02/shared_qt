#include <boxes.h>
#include <QtCore>
#include <QWidget>
#include <QObject>
#include <QMainWindow>
#include <QDockWidget>
#include <vector>
#include <QString>
#include <QGroupBox>
#include <QVBoxLayout>
#include <QFrame>

//This is the implementation for the Vertical Box
VerticalBox::VerticalBox(QWidget *parent, const QString& title): QWidget{parent}
{
    main = new QVBoxLayout(this);

    box = new QGroupBox(title, this);
    boxLayout = new QVBoxLayout(box);

    frame = new QFrame(box);
    frameLayout = new QVBoxLayout(frame);

    box->setLayout(boxLayout);
    boxLayout->addWidget(frame);

    
    main->addWidget(box);

}

void VerticalBox::addWidgets(const std::vector<QWidget*> &widgets)
{
    for (QWidget *widget : widgets)
    {
        if (widget)
        {
            frameLayout->addWidget(widget);
        }
        
    }

}
