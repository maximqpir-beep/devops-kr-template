# Команды для скриншотов

Команды предназначены для Git Bash. Выполняйте по одному блоку. Нужны Git и Python 3.
Это воспроизведение сохранённых этапов, выполненных при подготовке работы, а не новая работа с основной веткой.

## 1. Получить рабочую копию

Старая папка `devops-kr-template.git` — bare-копия без рабочих файлов. Откройте новый Git Bash на рабочем столе и создайте отдельную рабочую папку:

```bash
git clone https://github.com/maximqpir-beep/devops-kr-template.git devops-kr-report
cd devops-kr-report
git fetch evidence/stages.bundle 'refs/heads/report/*:refs/heads/report/*'
```

Архив и эта инструкция есть в `main` после слияния PR. Сохраните эту страницу в браузере: при переключении на старые состояния файлов инструкции в рабочей папке не будет.

## 2. История до rebase — СКРИНШОТ

```bash
git switch report/01-dirty
git log --oneline -4
```

Ожидаются четыре коммита: feat, test, wip и fix.

## 3. История и код после rebase — ДВА СКРИНШОТА

```bash
git switch report/02-clean
git log --oneline -3
```

```bash
cat validator.py
```

Новый коммит один; функции `validate_inn` нет. Старые коммиты преподавателя остаются в истории.

## 4. Воспроизвести конфликт — СКРИНШОТ

Настройки автора задаются только в этой рабочей копии:

```bash
git config user.name maximqpir-beep
git config user.email 230380816+maximqpir-beep@users.noreply.github.com
git switch -c report/conflict-demo report/02-clean
git merge report/instructor
git status --short
cat validator.py
```

Сообщение CONFLICT ожидаемо. Сфотографируйте файл с `<<<<<<<`, `=======`, `>>>>>>>` (можно открыть `validator.py` в редакторе). Есть также конфликт старого пути тестов — он возник из-за переноса в `tests/`.

После скриншота отмените только это демонстрационное слияние и откройте сохранённое разрешённое состояние:

```bash
git merge --abort
git switch report/03-resolved
cat validator.py
```

СКРИНШОТ: видны `validate_phone`, `validate_email`, `validate_snils`; маркеров конфликта нет. Если файл не помещается, сделайте несколько скриншотов.

```bash
python -m unittest discover -s tests -v
```

Дополнительный скриншот: три успешных тестовых метода.

## 5. Итоговая история — СКРИНШОТ

```bash
git switch main
git pull --ff-only origin main
git log --oneline --graph -5
```

Откройте вкладку Pull requests → Closed на GitHub и сохраните ссылку на слитый PR, сделайте скриншот его состояния Merged.

## 6. Три remote и зеркало

Этот этап нужно выполнить отдельно: зеркало ещё не создано.
Создайте ПУСТОЙ `devops-kr-mirror` на Gitverse или GitLab (варианты из методички). Ниже пример для Gitverse. Замените `ВАШ_ЛОГИН` на свой логин Gitverse.

```bash
git remote add upstream https://gitverse.ru/dgimatdinov/devops-kr-template.git
git remote add mirror https://gitverse.ru/ВАШ_ЛОГИН/devops-kr-mirror.git
git remote set-url --add --push origin https://github.com/maximqpir-beep/devops-kr-template.git
git remote set-url --add --push origin https://gitverse.ru/ВАШ_ЛОГИН/devops-kr-mirror.git
git remote -v
```

СКРИНШОТ: три имени remote; у origin два адреса push. Оба адреса добавляются явно, чтобы push не отправлялся только в зеркало.

```bash
git push origin main
```

При необходимости авторизуйтесь на соответствующем сервисе. Если есть ошибка, остановитесь и пришлите её текст; не используйте force.

```bash
git ls-remote origin refs/heads/main
git ls-remote mirror refs/heads/main
```

Ожидается одинаковый SHA. СКРИНШОТЫ: страницы основного репозитория и зеркала с итоговым коммитом.

Не отправляйте `report/*` в основную ветку: это вспомогательные локальные ветки для воспроизведения этапов.

## Чек-лист сдачи

- [ ] Скриншот трёх remote.
- [ ] Четыре коммита до rebase.
- [ ] Чистая история и код после rebase.
- [ ] Конфликт до разрешения и итоговый код.
- [ ] Ссылка на слитый PR.
- [ ] Скриншоты основного репозитория и зеркала.
- [ ] Финальная история main.
- [ ] Подготовка к устным вопросам на странице 8 методички.
