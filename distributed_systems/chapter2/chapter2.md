-- Architectural styles 
   - an Important goal of distributed system is to provide an abstract layer between the application layer and the underlying platform
   - A component is  a well defined modular unit with requirements and provide interface which is replaceble within its environment
   - connector - a mechanism that mediates communication or coopertaion among components.
          - Layered Architectures
          - Service-oriented architectures
          - Publish-subscribe architectures

          Layed architecture
           - component is layer l1 can make a downward call to a component at a lower layer l2 and generally expects a response. Only on exceptional scenarios will an upward call be made to a higher layer 