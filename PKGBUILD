# Maintainer: Prayz Jomba <prayzjomba@protonmail.com>
pkgname=ywatch
pkgver=0.6.3
pkgrel=1
pkgdesc="Watch youtube videos with mpv while saving the video to disk."
arch=(any)
url="https://github.com/prayzjomba/ywatch.git"
license=('GPL')
depends=('youtube-dl' 'xclip' 'mpv' 'python-rich' 'python-pyperclip' 'python-func-timeout')
makedepends=('git' 'make' 'python-setuptools')
provides=(yw)
install=
changelog=
source=("$pkgname-$pkgver"::"git+$url#branch=$pkgver")
md5sums=('SKIP')

build() {
	cd "$pkgname-$pkgver"
	python setup.py build
}


package() {
	cd "$pkgname-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1
}
