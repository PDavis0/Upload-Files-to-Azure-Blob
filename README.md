# Upload-Files-to-Azure-Blob
Uploads all the files that has not been uploaded to an Azure storage blob.

To use this:
  Put script in current directory of the pictures.
  run cmd line "python moveToAzure.py"

  Note: one will have to update the account name, container, and key for their azure account. 
  It is hard coded. BAD practice in production as one would want expiring keys perhaps put on 
  the root directory. Never hard code, but this is fast development work.
