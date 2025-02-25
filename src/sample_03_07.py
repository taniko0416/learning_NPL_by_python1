import json

import sqlitedatastore as datastore
import solrindexer as indexer

if __name__ == '__main__':
    datastore.connect()
    data = []
    for doc_id in datastore.get_all_ids(limit=-1):
        row = datastore.get(doc_id, ['id','content','meta_info'])
        # Solrへの登録するデータ構造へ変換
        meta_info = json.load(row['meta_info'])
        data.append(
            {
                'id'                :str(row['id']),
                'doc_id_i'          :row['id'],
                'contebt_txt_ja'    :row['content'],
                'title_txt_ja'      :meta_info['title'],
                'url_s'             :meta_info['url']
            }
        )
# Solrへの登録を実行
indexer.load('doc',data)
datastore.close() 