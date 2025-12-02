1.  **Web App (Flask):** 
2.  **Cache Layer (Redis):** 
3.  **Data Store (PostgreSQL):** 

acessar `http://localhost:5000/`:
1.  O container `web-app` conecta no `cache-layer` e incrementa o contador.
2.  O container `web-app` conecta no `data-store` e insere um registro de timestamp.
3.  O resultado JSON confirma que ambas as operações (Cache e DB) foram bem-sucedidas.

```bash
docker compose up -d --build