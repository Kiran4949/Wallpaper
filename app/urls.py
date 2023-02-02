from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm, MySetPasswordForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),

    path('about/', views.about, name="about"),

    path('contact', views.contact, name="contact"),

    path('signup/', views.signup, name='signup'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('login/', views.loginUser, name="login"),

    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 

    path('login/password_reset', auth_views.PasswordResetView.as_view(template_name= 'password_reset.html', form_class=MyPasswordResetForm), name='password_reset'), 
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_done.html'), name='password_reset_done'), 
    path('password_reset_confirm<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'), name='password_reset_complete'),

    path('wallpaper-img/<int:pk>', views.WallpaperDetailView.as_view(), name='wallpaper-img'), 

    path('nature/', views.Nature.as_view(), name='nature'),

    path('space/', views.Space.as_view(), name='space'),

    path('country/', views.Country.as_view(), name='country'),

    path('animal/', views.Animal.as_view(), name='animal'),

    path('tajmahal/', views.Tajmahal.as_view(), name='tajmahal'),

    path('car/', views.Car.as_view(), name='car'),

    path('flower/', views.Flower.as_view(), name='flower'),

    path('windows/', views.Window.as_view(), name='windows'),

    path('cartoon/', views.Cartoon.as_view(), name='cartoon'),

    path('mobile/', views.Mobile.as_view(), name='mobile'),

    path('mobile/signup', views.signup, name='signup' ),
    path('mobile/login', views.loginUser, name="login"),
    path('mobile/about', views.about, name="about"),
    path('mobile/contact', views.contact, name="contact"),
    path('mobile/nature', views.Nature.as_view(), name="nature"),
    path('mobile/space', views.Space.as_view(), name='space'),
    path('mobile/country', views.Country.as_view(), name='country'),
    path('mobile/animal', views.Animal.as_view(), name='animal'),
    path('mobile/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('mobile/car', views.Car.as_view(), name='car'),
    path('mobile/flower', views.Flower.as_view(), name='flower'),
    path('mobile/windows', views.Window.as_view(), name='windows'),
    path('mobile/cartoon', views.Cartoon.as_view(), name='cartoon'),

    path('nature/space', views.Space.as_view(), name='space'),
    path('nature/country', views.Country.as_view(), name='country'),
    path('nature/animal', views.Animal.as_view(), name='animal'),
    path('nature/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('nature/car', views.Car.as_view(), name='car'),
    path('nature/flower', views.Flower.as_view(), name='flower'),
    path('nature/windows', views.Window.as_view(), name='windows'),
    path('nature/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('nature/mobile', views.Mobile.as_view(), name='mobile'),
    path('nature/signup', views.signup, name='signup' ),
    path('nature/login', views.loginUser, name="login"),
    path('nature/about', views.about, name="about"),
    path('nature/contact', views.contact, name="contact"),

    path('space/nature', views.Nature.as_view(), name='nature'),
    path('space/country', views.Country.as_view(), name='country'),
    path('space/animal', views.Animal.as_view(), name='animal'),
    path('space/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('space/car', views.Car.as_view(), name='car'),
    path('space/flower', views.Flower.as_view(), name='flower'),
    path('space/windows', views.Window.as_view(), name='windows'),
    path('space/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('space/mobile', views.Mobile.as_view(), name='mobile'),
    path('space/signup', views.signup, name='signup' ),
    path('space/login', views.loginUser, name="login"),
    path('space/about', views.about, name="about"),
    path('space/contact', views.contact, name="contact"),

    path('country/nature', views.Nature.as_view(), name='nature'),
    path('country/space', views.Space.as_view(), name='space'),
    path('country/animal', views.Animal.as_view(), name='animal'),
    path('country/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('country/car', views.Car.as_view(), name='car'),
    path('country/flower', views.Flower.as_view(), name='flower'),
    path('country/windows', views.Window.as_view(), name='windows'),
    path('country/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('country/mobile', views.Mobile.as_view(), name='mobile'),
    path('country/signup', views.signup, name='signup' ),
    path('country/login', views.loginUser, name="login"),
    path('country/about', views.about, name="about"),
    path('country/contact', views.contact, name="contact"),

    path('animal/nature', views.Nature.as_view(), name='nature'),
    path('animal/space', views.Space.as_view(), name='space'),
    path('animal/country', views.Country.as_view(), name='country'),
    path('animal/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('animal/car', views.Car.as_view(), name='car'),
    path('animal/flower', views.Flower.as_view(), name='flower'),
    path('animal/windows', views.Window.as_view(), name='windows'),
    path('animal/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('animal/mobile', views.Mobile.as_view(), name='mobile'),
    path('animal/signup', views.signup, name='signup' ),
    path('animal/login', views.loginUser, name="login"),
    path('animal/about', views.about, name="about"),
    path('animal/contact', views.contact, name="contact"),

    path('tajmahal/nature', views.Nature.as_view(), name='nature'),
    path('tajmahal/space', views.Space.as_view(), name='space'),
    path('tajmahal/country', views.Country.as_view(), name='country'),
    path('tajmahal/animal', views.Animal.as_view(), name='animal'),
    path('tajmahal/car', views.Car.as_view(), name='car'),
    path('tajmahal/flower', views.Flower.as_view(), name='flower'),
    path('tajmahal/windows', views.Window.as_view(), name='windows'),
    path('tajmahal/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('tajmahal/mobile', views.Mobile.as_view(), name='mobile'),
    path('tajmahal/signup', views.signup, name='signup' ),
    path('tajmahal/login', views.loginUser, name="login"),
    path('tajmahal/about', views.about, name="about"),
    path('tajmahal/contact', views.contact, name="contact"),

    path('car/nature', views.Nature.as_view(), name='nature'),
    path('car/space', views.Space.as_view(), name='space'),
    path('car/country', views.Country.as_view(), name='country'),
    path('car/animal', views.Animal.as_view(), name='animal'),
    path('car/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('car/flower', views.Flower.as_view(), name='flower'),
    path('car/windows', views.Window.as_view(), name='windows'),
    path('car/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('car/mobile', views.Mobile.as_view(), name='mobile'),
    path('car/signup', views.signup, name='signup' ),
    path('car/login', views.loginUser, name="login"),
    path('car/about', views.about, name="about"),
    path('car/contact', views.contact, name="contact"),

    path('flower/nature', views.Nature.as_view(), name='nature'),
    path('flower/space', views.Space.as_view(), name='space'),
    path('flower/country', views.Country.as_view(), name='country'),
    path('flower/animal', views.Animal.as_view(), name='animal'),
    path('flower/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('flower/car', views.Car.as_view(), name='car'),
    path('flower/windows', views.Window.as_view(), name='windows'),
    path('flower/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('flower/mobile', views.Mobile.as_view(), name='mobile'),
    path('flower/signup', views.signup, name='signup' ),
    path('flower/login', views.loginUser, name="login"),
    path('flower/about', views.about, name="about"),
    path('flower/contact', views.contact, name="contact"),

    path('windows/nature', views.Nature.as_view(), name='nature'),
    path('windows/space', views.Space.as_view(), name='space'),
    path('windows/country', views.Country.as_view(), name='country'),
    path('windows/animal', views.Animal.as_view(), name='animal'),
    path('windows/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('windows/car', views.Car.as_view(), name='car'),
    path('windows/flower', views.Flower.as_view(), name='flower'),
    path('windows/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('windows/mobile', views.Mobile.as_view(), name='mobile'),
    path('windows/signup', views.signup, name='signup' ),
    path('windows/login', views.loginUser, name="login"),
    path('windows/about', views.about, name="about"),
    path('windows/contact', views.contact, name="contact"),

    path('cartoon/nature', views.Nature.as_view(), name='nature'),
    path('cartoon/space', views.Space.as_view(), name='space'),
    path('cartoon/country', views.Country.as_view(), name='country'),
    path('cartoon/animal', views.Animal.as_view(), name='animal'),
    path('cartoon/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('cartoon/car', views.Car.as_view(), name='car'),
    path('cartoon/flower', views.Flower.as_view(), name='flower'),
    path('cartoon/windows', views.Window.as_view(), name='windows'),
    path('cartoon/mobile', views.Mobile.as_view(), name='mobile'),
    path('cartoon/signup', views.signup, name='signup' ),
    path('cartoon/login', views.loginUser, name="login"),
    path('cartoon/about', views.about, name="about"),
    path('cartoon/contact', views.contact, name="contact"),

    path('about/nature', views.Nature.as_view(), name='nature'),
    path('about/space', views.Space.as_view(), name='space'),
    path('about/country', views.Country.as_view(), name='country'),
    path('about/animal', views.Animal.as_view(), name='animal'),
    path('about/tajmahal', views.Tajmahal.as_view(), name='tajmahal'),
    path('about/car', views.Car.as_view(), name='car'),
    path('about/flower', views.Flower.as_view(), name='flower'),
    path('about/windows', views.Window.as_view(), name='windows'),
    path('about/mobile', views.Mobile.as_view(), name='mobile'),
    path('about/cartoon', views.Cartoon.as_view(), name='cartoon'),
    path('about/signup', views.signup, name='signup' ),
    path('about/login', views.loginUser, name="login"),
    path('about/contact', views.contact, name="contact"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
