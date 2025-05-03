// ヘッダーの処理
document.addEventListener('DOMContentLoaded', function() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const mainNavMobile = document.querySelector('.main-nav-mobile');
    const mobileNavItemsWithSubmenu = document.querySelectorAll('.main-nav-mobile .has-submenu > a');

    // ハンバーガーメニューのクリック処理
    if (hamburgerMenu && mainNavMobile) {
        hamburgerMenu.addEventListener('click', function() {
            mainNavMobile.classList.toggle('active');
        });
    }

    // モバイルナビゲーションのサブメニュー開閉処理 (必要に応じて)
    mobileNavItemsWithSubmenu.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            this.parentNode.classList.toggle('open');
            const submenu = this.nextElementSibling;
            if (submenu) {
                submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
            }
        });
    });

    // PC 用ドロップダウンメニューの処理 (既存のコードがここにある場合はそのまま)
    const navItemsWithDropdown = document.querySelectorAll('header > nav > div');
    navItemsWithDropdown.forEach(item => {
        const dropdown = item.querySelector('div');
        const link = item.querySelector('a');
        if (dropdown && link) {
            item.addEventListener('mouseenter', function() {
                dropdown.style.display = 'block';
            });
            item.addEventListener('mouseleave', function() {
                dropdown.style.display = 'none';
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const select = document.querySelector('.language-select');
    if (select) {
        let isSelectOpen = false;
        select.addEventListener('click', () => {
            isSelectOpen = !isSelectOpen;
        });
    } else {
        console.error('要素の取得に失敗しました。');
    }
});

// エラーメッセージ(警報)
document.addEventListener('DOMContentLoaded', function() {
    const convertButton = document.querySelector('.btn-area .btn-aa button'); // 変換ボタンを取得
    const btnAaContainer = document.querySelector('.btn-area .btn-aa'); // エラーメッセージを挿入する基準要素

    if (convertButton && btnAaContainer) {
        convertButton.addEventListener('click', function() {
            // エラーメッセージ要素を作成
            const errorMessage = document.createElement('div');
            errorMessage.textContent = '現在この機能は使えません';
            errorMessage.style.color = 'red';
            errorMessage.style.marginTop = '10px'; // 必要に応じてマージンを追加
            errorMessage.classList.add('error-message'); // クラスを追加 (CSS でスタイルを当てる場合)

            // btnAaContainer の直後にエラーメッセージを挿入
            btnAaContainer.parentNode.insertBefore(errorMessage, btnAaContainer.nextSibling);

            // (オプション) 一定時間後にエラーメッセージを削除する場合
            // setTimeout(function() {
            //     errorMessage.remove();
            // }, 3000); // 3秒後に削除
        });
    }
});

// process_video.pyにurlをおくる関数。
// pythonファイルの結果が返ってきたら、持ってたurlと結果の.txtのテキストデータを返す。
async function processUrls() {
    const urlsTextarea = document.getElementById('youtubeUrls');
    const outputArea = document.getElementById('outputArea');
    const urls = urlsTextarea.value.trim().split('\n').filter(url => url !== '');

    for (const url of urls) {
        outputArea.innerHTML += `<p>処理中: ${url}</p>`;
        const response = await fetch('/process_url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url }),
        });

        if (response.ok) {
            const data = await response.json();
            outputArea.innerHTML += `<p>URL: ${url}</p><p>${data.text}</p><hr>`; 
        } else {
            outputArea.innerHTML += `<p class="error">エラー: ${url} の処理に失敗しました。</p><hr>`;
        }
    }
}