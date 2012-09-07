$(function () {
	var Event = Backbone.Model.extend()
	
	var Events = Backbone.Collection.extend({
		model: Event,
		url: '/api/v1/events/'
	});
	
	var EventsView = Backbone.View.extend({
		initialize: function(){
			_.bindAll(this);
			this.collection.bind('reset', this.addAll);
			this.collection.bind('add', this.addOne);
			this.collection.bind('change', this.change);
			this.collection.bind('destroy', this.destroy);
		},
		render: function(){
			$(this.el).fullCalendar({
				header: {
					left: 'prev,next today',
					center:'title',
					right: 'month,basicWeek,basicDay',
					ignoreTimezone: true
				},
				selectable: true,
				selectHelper: true,
				editable: true,
				select: this.select,
				eventClick: this.eventClick,
				eventDrop: this.eventDropOrResize,
				eventResize: this.eventDropOrResize
			});
			console.log(this.collection)
			return this;
		},
		addAll: function(){
			$(this.el).fullCalendar('addEventSource', this.collection.toJSON());
		},
		select: function(startDate, endDate){
			var eventView = new EventView();
			eventView.collection = this.collection;
			eventView.model = new Event({start: startDate, end: endDate});
			eventView.render();
		},
		eventClick: function(fcEvent) {
			var eventView = new EventView();
			eventView.model = this.collection.get(fcEvent.resource_uri)
			eventView.render();
		},
		addOne: function(event) {
			$(this.el).fullCalendar('renderEvent', event.toJSON())
			console.log("in addone")
		},
		change: function(event) {
			console.log("change called", event)
			var fcEvent = $(this.el).fullCalendar('clientEvents', event.attributes.id)[0];
			fcEvent.title = event.attributes.title;
			fcEvent.color = event.attributes.color;
			fcEvent.description = event.attributes.description;
			fcEvent.start = event.attributes.start;
			fcEvent.end = event.attributes.end;
			$(this.el).fullCalendar('updateEvent', fcEvent) 
		},
		eventDropOrResize: function(fcEvent) {
			console.log(fcEvent)
			this.collection.get(fcEvent.resource_uri).save({start: fcEvent.start, end: fcEvent.end});
		},
		destroy: function(event) {
			console.log(event)
			$(this.el).fullCalendar('removeEvents', event.attributes.id)
		}
		
	});
	
	var EventView = Backbone.View.extend({
		el: $('#eventDialog'),
		initialize: function(){
			_.bindAll(this);
		},
		render: function() {
			var buttons = {'Save': this.save};
			if(!this.model.isNew()){
				_.extend(buttons, {'Delete': this.destroy});
			}
			_.extend(buttons, {'Cancel': this.close})
			
			$(this.el).dialog({
				modal: true,
				title: (this.model.isNew() ? 'New' : 'Edit') + ' Event',
				buttons: buttons,
				open: this.open
			})
			
			return this;
		},
		open: function(){
			this.$('#title').val(this.model.get('title'));
			this.$('#color').val(this.model.get('color'));
			this.$('#description').val(this.model.get('description'));
			this.$('#start-time').val("")
			this.$('#start-date').val("")
			this.$('#end-time').val("")
			this.$('#end-date').val("")
			
			if (!this.model.isNew()){
				var startTimezonePos = this.model.get('start').lastIndexOf('+')
				var startDateTimeSplit = this.model.get('start').indexOf('T');
				var endTimezonePos = this.model.get('end').lastIndexOf('+')
				var endDateTimeSplit = this.model.get('end').indexOf('T');
			
				this.$('#start-time').val(this.model.get('start').slice(startDateTimeSplit+1, startTimezonePos));
				this.$('#end-time').val(this.model.get('end').slice(endDateTimeSplit+1, endTimezonePos));
				this.$('#start-date').val(dateUnformat(this.model.get('start').slice(0, startDateTimeSplit)));
				this.$('#end-date').val(dateUnformat(this.model.get('end').slice(0, endDateTimeSplit)));
				
				this.$('#timezone').val(this.model.get('start').slice(startTimezonePos))
				
			}
			
		},
		close: function(){
			$(this.el).dialog("close");
		},
		save: function(){
			console.log(dateFormat(this.$('#start-date').val()))
			this.model.set({start: dateFormat(this.$('#start-date').val()) + 'T' + this.$('#start-time').val() + this.$('#timezone').val(), 
								end: dateFormat(this.$('#end-date').val()) + 'T' + this.$('#end-time').val() + this.$('#timezone').val()})
								
			this.model.set({'title': this.$('#title').val(), 'color': this.$('#color').val(), 'description': this.$('#description').val()})
			if(this.model.isNew()){
				this.collection.create(this.model, {success: this.close, wait:true})
				
			} else {
				this.model.save({}, {success: this.close, wait:true})
			}
		},
		destroy: function() {
			this.model.destroy({success: this.close})
		}
	});
	
	var events = new Events();
	new EventsView({el: $("#calendar"), collection: events}).render();
	events.fetch();
	
})
