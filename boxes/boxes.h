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

class VerticalBox: public QWidget
{
    Q_OBJECT

    public:
        explicit VerticalBox(QWidget *parent = nullptr, const QString& title = "");
        ~VerticalBox() = default;

        void addWidgets(const std::vector<QWidget*> &widgets);
    
    private:

        QGroupBox *box = nullptr;
        QVBoxLayout *boxLayout = nullptr;
        QFrame *frame = nullptr;
        QVBoxLayout *frameLayout = nullptr;
        QVBoxLayout *main = nullptr;

};
