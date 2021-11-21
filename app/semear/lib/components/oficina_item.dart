import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:semear/pages/oficina_detalhes/oficina_detalhes.dart';

import '../envs.dart';

class OficinaItemComponent extends StatelessWidget {
  OficinaItemComponent({required this.oficina, this.isSubscribed = true});

  final Map<String, dynamic> oficina;
  final bool isSubscribed;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(bottom: 25),
      child: Column(
        children: [
          oficina["imagens"].length > 0
              ? Container(
                  height: 200,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.all(Radius.circular(14)),
                    image: DecorationImage(
                      image: NetworkImage(url_semear + oficina["imagens"][0]),
                      fit: BoxFit.cover,
                    ),
                  ),
                )
              : Container(),
          Container(
            padding: EdgeInsets.all(25),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Flexible(
                      child: Text(
                        oficina['nome'],
                        overflow: TextOverflow.ellipsis,
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 25,
                        ),
                      ),
                    ),
                    Text(
                      oficina['horario'],
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                Text(
                  "Prof." + oficina['orientador__user__nome'],
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 17,
                  ),
                ),
                Divider(
                  color: Color(0x01000001),
                ),
                isSubscribed
                    ? TextButton(
                        onPressed: () {
                          Navigator.of(context).push(
                            CupertinoPageRoute(
                              builder: (ctx2) => OficinaDetalhesPage(
                                oficinaId: oficina['id'],
                              ),
                            ),
                          );
                        },
                        child: Padding(
                          padding: const EdgeInsets.all(2.0),
                          child: Text(
                            "Ver mais",
                            style: TextStyle(
                              fontSize: 14,
                              color: Colors.white,
                            ),
                          ),
                        ),
                        style: TextButton.styleFrom(
                          backgroundColor: Color(0xff020129),
                        ),
                      )
                    : Container(),
              ],
            ),
          ),
        ],
      ),
      decoration: BoxDecoration(
        color: Color(0xffFB8500),
        borderRadius: BorderRadius.all(Radius.circular(14)),
      ),
    );
  }
}
