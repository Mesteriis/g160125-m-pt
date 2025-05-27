### 1. Временное сохранение (до закрытия терминала)
Если API-ключ нужен только для текущего сеанса консоли, можно установить его так
```bash
set API_KEY=your_api_key_here
```
Проверить, что переменная установлена
```bash
echo %API_KEY%
```
Использовать в `curl`-запросе
```bash
curl -H Authorization Bearer %API_KEY% httpsapi.example.comdata
```
⚠️ Этот способ работает только пока открыт текущий терминал.

---

### 2. Постоянное сохранение (переживает перезапуск)
Чтобы API-ключ сохранялся между сеансами, его нужно добавить в переменные окружения Windows

#### Через командную строку (`cmd`)
```bash
setx API_KEY your_api_key_here
```
Проверить
```bash
echo %API_KEY%
```
⚠️ Важно после `setx` переменная доступна только в новых терминалах, в текущем ее не будет.

#### Через PowerShell
```powershell
[System.Environment]SetEnvironmentVariable(API_KEY, your_api_key_here, User)
```
Проверить
```powershell
echo $envAPI_KEY
```
Теперь ключ сохранится между перезагрузками.

---

### 3. Использование в `curl`
После установки API-ключа в переменные окружения можно делать `curl`-запросы так
```bash
curl -H Authorization Bearer %API_KEY% httpsapi.example.comdata
```
или в PowerShell
```powershell
curl -H Authorization Bearer $envAPI_KEY httpsapi.example.comdata
```

Если ключ нужно удалить
```bash
setx API_KEY 
```

Это самый удобный способ, если ключ часто используется.